import random

from interface import printGuess
from colorama import Fore

#Decrease words from wordscores given information green (correct place)
def solveGreen(wordscores,guessWord, toEvaluate, guessResult):
    wordscores.pop(guessWord,None)
    key_list= list(wordscores)
    indices = []
    for i in range(5):
        if(guessResult[i] == Fore.GREEN):
            toEvaluate[i] = guessWord[i]
            indices.append(i)
    for wordsLeft in key_list:
        for i in indices:
            if (wordsLeft[i] not in toEvaluate[i]):
                wordscores.pop(wordsLeft,None)
                break
    return wordscores, toEvaluate

def solveYellow(wordscores,guessWord, toEvaluate, guessResult):
    wordscores.pop(guessWord,None)
    key_list= list(wordscores)
    indices = []
    for i in range(5):
        if(guessResult[i] == Fore.YELLOW):
            toEvaluate[i]= toEvaluate[i].replace(guessWord[i], '')
            indices.append(i)
    for wordsLeft in key_list:
        for i in indices:
            if (guessWord[i] not in wordsLeft or wordsLeft[i] not in toEvaluate[i]):
                wordscores.pop(wordsLeft,None)
                break
    return wordscores, toEvaluate

def solveGray(wordscores,guessWord, toEvaluate, guessResult):
    wordscores.pop(guessWord,None)
    key_list= list(wordscores)
    indices = []
    for i in range(5):
        if(guessResult[i] == Fore.WHITE):
            indices.append(i)
    
    for i in indices:
        toEvaluate[i] = toEvaluate[i].replace(guessWord[i], '')

    for wordsLeft in key_list:
        for i in indices:
            if(wordsLeft[i] not in toEvaluate[i]):
                wordscores.pop(wordsLeft,None)
                break
    return wordscores, toEvaluate

def solveWithAll(wordscores,guessWord, toEvaluate, guessResult):
    wordscores,toEvaluate = solveGreen(wordscores,guessWord, toEvaluate, guessResult)
    wordscores,toEvaluate = solveYellow(wordscores,guessWord, toEvaluate, guessResult)
    wordscores,toEvaluate = solveGray(wordscores,guessWord, toEvaluate, guessResult)
    return wordscores, toEvaluate

def solveTree(wordscores,guessWord,tree, guessResult):
    filter = tree[guessWord][str(guessResult)]
    for word in list(wordscores):
        if word not in filter:
            wordscores.pop(word,None)
    return wordscores