from solver import *
from preprocess import *
from interface import *

if __name__ == '__main__':
    words = getWords()

    ''' Line 8 and 9 interchangable for scoring words with different methods'''
    wordScore = calcWordScorebyOccurence(words)
    # wordScore = calcWordScorebyPosition(words)

    '''Get a random word to use as a target to guess'''
    targetWord = getRandomTarget(list(wordScore))
    targetWord = 'MAMAS'
    printGuess(targetWord,'-----')

    '''Preprocess'''
    toEvaluate = [string.ascii_uppercase for _ in range(5)]

    '''Start guessing'''
    guess = list(wordScore)[0]
    printGuess(guess,targetWord)
    evaluation = evalGuess(guess,targetWord)
    while(not(checkGuess(evaluation))):
        wordScore,toEvaluate = solveWithAll(wordScore,guess, toEvaluate, evaluation)
        guess = list(wordScore)[0]
        evaluation = evalGuess(guess,targetWord)
        printGuess(guess,targetWord)