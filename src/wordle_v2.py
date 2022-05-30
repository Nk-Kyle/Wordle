from solver import *
from preprocess import *
from interface import *
import pickle

if __name__ == '__main__':
    words = getWords()

    ''' Line 8 and 9 interchangable for scoring words with different methods'''
    # wordScore = calcWordScorebyOccurence(words)
    wordScore = calcWordScorebyPosition(words)

    '''Get a random word to use as a target to guess'''
    targetWord = getRandomTarget(list(wordScore))
    targetWord = 'MAMAS'
    printGuess(targetWord,'-----')

    '''Get the decision tree from file'''
    with open('resources/tree.pkl', 'rb') as f:
        tree = pickle.load(f)


    '''Start guessing'''
    guess = list(wordScore)[0]
    printGuess(guess,targetWord)
    evaluation = evalGuess(guess,targetWord)
    while(not(checkGuess(evaluation))):
        wordScore = solveTree(wordScore,guess, tree, evaluation)
        guess = list(wordScore)[0]
        evaluation = evalGuess(guess,targetWord)
        printGuess(guess,targetWord)