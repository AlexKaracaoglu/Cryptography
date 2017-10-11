# Alex Karacaoglu and Brendan Duhamel
# Project 1: Automated Cryptanalysis of Monoalphabetic Substitution Cipher

import string
import math
import random
import itertools

#Code to set up the text file, open and then get rid of irrelevant stuff
def setup(filename):
    f = open(filename,'rb')
    s = f.read()
    s = s.translate(None,string.whitespace)
    s = s.translate(None,string.punctuation)
    s = s.translate(None,string.digits)
    s = s.replace('\x94','')
    s = s.replace('\x93','')
    s = s.replace('\x92','')
    s = s.lower()
    return s

#count number of occuraces of a in the string s
def countSets(a,s):
    return s.count(a)

#append string b to the end of a
def append(a,b):
    s = "".join((a,b))
    return s

#setting up the dictionary that we will be using   
def setUpDictionary(s1,s2,s3):
    dictionary = {}
    for i in range(97,123):
        for j in range(97,123):
            iC = chr(i)
            jC = chr(j)
            a = append(iC,jC)
            b1 = float(countSets(a,s1)) + 26
            b2 = float(countSets(a,s2)) + 26
            b3 = float(countSets(a,s3)) + 26
            lis = []
            fulList = []
            for k in range(97,123):
                newSub = append(a,chr(k))
                countNewSubs1 = countSets(newSub,s1) +1
                countNewSubs2 = countSets(newSub,s2) +1
                countNewSubs3 = countSets(newSub,s3) +1
                freq = (countNewSubs1 + countNewSubs2 + countNewSubs3) / (b1+b2+b3)
                lis.append(freq)
            dictionary[a] = lis
    return dictionary

##### GLOBAL VARIABLES #####
s1 = setup('jane.txt')
s2 = setup('tale.txt')
s3 = setup('heart.txt')
dictionary = setUpDictionary(s1,s2,s3)

#generates a random permutation of the 26 letters of the alphabet and can be used to shuffle around the letters of the cipher text
def permute():
    a = list(string.ascii_lowercase)
    random.shuffle(a)
    return a

#Used to rearrange the letters so we can make many passes through to find the best decryption
def rearrange(text,permutation):
    new = text
    for i in range(len(permutation)):
        new = new.replace(chr(i+97),chr(ord(permutation[i])-32))
    new = new.lower()
    return new

#Scoring algorithm
def score(text, dictionary):
    score = 0
    for i in range(len(text)-2):
        a = append(text[i],text[i+1])
        b = text[i+2]
        b = ord(b) - 97
        value = dictionary[a][b]
        value = -1 * math.log(value)
        score = score + value
    return score

#Takes two letters in a string, and swaps them
def swapString(string,a,b):
    s = string
    s = s.replace(a,chr(ord(b)-32))
    s = s.replace(b,chr(ord(a)-32))
    s = s.lower()
    return s

#Iterates through all possible moves and calculates the best one according to the scoring alg
def bestSingleMove(text,dictionary):
    bestScore = score(text,dictionary)
    bestText = text
    allCombos = list(itertools.combinations(string.ascii_lowercase,2))
    for i in range(len(allCombos)):
        tempText = swapString(text,allCombos[i][0],allCombos[i][1])
        tempScore = score(tempText,dictionary)
        if tempScore < bestScore:
            bestText = tempText
            bestScore = tempScore
    return (bestText,bestScore)

#Keeps doing the best move until you reach a local minimum (smaller = better) score
def untilMinimal(text):
    old_score = 0
    new_score = score(text,dictionary)
    new_text = text
    while (old_score != new_score):
        old_score = new_score
        a = bestSingleMove(new_text,dictionary)
        new_text = a[0]
        new_score = a[1]
    return (new_score,new_text)

#Does a series of 200 minimal trials and returns the best score and the best text
def manyMinimalTrials(text):
    best_score = score(text,dictionary)
    best_text = text
    for i in range(200):
        print str(i)
        new_text = rearrange(text,permute())
        a = untilMinimal(new_text)
        temp_text = a[1]
        temp_score = a[0]
        if temp_score < best_score:
            best_score = temp_score
            best_text = temp_text
    return (best_score, best_text)
    
    
#Takes in a cipher text, no spaces and returns (Hopefully) the correct result
def go(text):
    a = manyMinimalTrials(text)
    final_text = a[1]
    return final_text   
