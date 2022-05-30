import string
import random
from interface import *
#Gets number of occurence of letter in word from wordlist
def calcAlphabetScorebyOccurence(wordlist):
    alphabetVal = {}
    for word in wordlist:
        for letter in set(word):
            alphabetVal[letter] = alphabetVal.get(letter, 0) + 1
    alphabetVal = sorted(alphabetVal.items(), key=lambda x: x[1], reverse=True)
    return dict(alphabetVal)

#Calculate score of each words from given wordlist and alphabet score
def calcWordScorebyOccurence(wordlist):
    alphabetVal= calcAlphabetScorebyOccurence(wordlist)
    wordScore = {}
    for word in wordlist:
        for letter in set(word):
            wordScore[word] = wordScore.get(word, 0) + alphabetVal.get(letter, 0)
    wordScore = sorted(wordScore.items(), key=lambda x: x[1], reverse=True)
    return dict(wordScore)

#Gets matrix of letters an occurence in position
def calcAlphabetScorebyPosition(wordlist):
    alphabetVal = {}
    for alphabet in string.ascii_uppercase:
        alphabetVal[alphabet] = [0 for _ in range (5)]
    for word in wordlist:
        for i in range(len(word)):
            alphabetVal[word[i]][i] += 1
    return alphabetVal

#Gets dictionary of word and its score using position occurence
def calcWordScorebyPosition(wordlist):
    alphabetScore = calcAlphabetScorebyPosition(wordlist)
    wordScore = {}
    for word in wordlist:
        for i in range(5):
            wordScore[word] = wordScore.get(word, 0) + alphabetScore[word[i]][i]
    wordScore = sorted(wordScore.items(), key=lambda x: x[1], reverse=True)
    return dict(wordScore)

#Get words from wordlist
def getWords():
    words = []
    with open('resources/wordlist', 'r') as f:
        for lines in f:
            words.append(lines.strip().upper())
    return words

def getRandomTarget(keys):
    return random.choice(keys)

def buildTree(wordlist):
    tree = {}
    for word in wordlist:
        tree[word] = {}
        for referWord in wordlist:
            if(word != referWord):
                eval = str(evalGuess(word, referWord))
                tree[word].setdefault(eval, [])
                tree[word][eval].append(referWord)
    return tree
