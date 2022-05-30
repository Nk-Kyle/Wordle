import datetime
import pickle
import threading
import string
from time import sleep
from solver import *
from preprocess import *
from interface import *
import copy


roundsTillFound = {}
data_lock = threading.Lock()

def mergeDictionary( dict_2):
    global roundsTillFound
    dict_3 = {**roundsTillFound, **dict_2}
    for key, value in dict_3.items():
        if key in roundsTillFound and key in dict_2:
                dict_3[key] = value + roundsTillFound[key]
    return dict_3

def evaluate(wordScore, words,tree):
    global roundsTillFound
    wordScoreMain = copy.deepcopy(wordScore)
    tempDict = {}
    
    for word in words:
        wordScore = copy.deepcopy(wordScoreMain)
        '''Get a random word to use as a target to guess'''
        targetWord = word
        guess = list(wordScore)[0]
        evaluation = evalGuess(guess,targetWord)
        n_guess = 1
        while(not(checkGuess(evaluation))):
            wordScore = solveTree(wordScore,guess, tree, evaluation)
            guess = list(wordScore)[0]
            evaluation = evalGuess(guess,targetWord)
            n_guess += 1
        tempDict[n_guess] = tempDict.get(n_guess,0) + 1
    with data_lock:
        roundsTillFound = mergeDictionary(tempDict)
    


if __name__ == '__main__':
    words = getWords()
    wordScore = calcWordScorebyPosition(words)
    print("using position and tree")
    # wordScore = calcWordScorebyOccurence(words)
    # print("using occurence and tree")
    # printGuess(targetWord,'-----')
    toEvaluate = [list(string.ascii_uppercase) for _ in range(5)]
    roundsTillFound = {}
    bins = 1
    threads = []
    start_time = datetime.datetime.now()
    with open('resources/tree.pkl', 'rb') as f:
        tree = pickle.load(f)
    for i in range(bins):
        threads.append(threading.Thread(target=evaluate, args=(wordScore,words[i*len(words)//bins:(i+1)*len(words)//bins], tree)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end_time = datetime.datetime.now()

    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    roundsTillFound = sorted(roundsTillFound.items(), key=lambda x: x[1], reverse=True)
    print(roundsTillFound)
    print(execution_time)
    
