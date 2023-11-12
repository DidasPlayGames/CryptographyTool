


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from numpy.linalg import norm


# Establish a global dictionary for the integer equivalent of a character, and frequency analysis
# Monogram values are held as decimal, meanwhile tetragrams are held as a percentage
conversionDictionary = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
corpusMonograms = [0.0855, 0.0160, 0.0316, 0.0387, 0.1210, 0.0218, 0.0209, 0.0496, 0.0733, 0.0022, 0.0081, 0.0421, 0.0253, 0.0717, 0.0747, 0.0207, 0.0010, 0.0633, 0.0673, 0.0894, 0.0268, 0.0106, 0.0183, 0.0019, 0.0172, 0.0011]
corpusBigrams = {"TH" : 2.71, "HE" : 2.33, "IN" : 2.03, "ER" : 1.78, "AN" : 1.61, "RE" : 1.41, "ES" : 1.32, "ON" : 1.32, "ST" : 1.25, "NT" : 1.17, "EN" : 1.13, "AT" : 1.12, "ED" : 1.08, "ND" : 1.07, "TO" : 1.07, "OR" : 1.06, "EA" : 1.00, "TI" : 0.99, "AR" : 0.98, "TE" : 0.98, "NG" : 0.89, "AL" : 0.88, "IT" : 0.88, "AS" : 0.87, "IS" : 0.86, "HA" : 0.83, "ET" : 0.76, "SE" : 0.73, "OU" : 0.72, "OF" : 0.71}
corpusTrigrams = {"THE" :  1.81, "AND" :  0.73, "ING" :  0.72, "ENT" :  0.42, "ION" :  0.42, "HER" :  0.36, "FOR" :  0.34, "THA" :  0.33, "NTH" :  0.33, "INT" :  0.32, "ERE" :  0.31, "TIO" :  0.31, "TER" :  0.30, "EST" :  0.28, "ERS" :  0.28, "ATI" :  0.26, "HAT" :  0.26, "ATE" :  0.25, "ALL" :  0.25, "ETH" :  0.24, "HES" :  0.24, "VER" :  0.24, "HIS" :  0.24, "OFT" :  0.22, "ITH" :  0.21, "FTH" :  0.21, "STH" :  0.21, "OTH" :  0.21, "RES" :  0.21, "ONT" :  0.20}
corpusTetragrams = {"tion" : 0.31, "nthe" : 0.27, "ther" : 0.24, "that" : 0.21, "ofth" : 0.19, "fthe" : 0.19, "thes" : 0.18, "with" : 0.18, "inth" : 0.17, "atio" : 0.17, "othe" : 0.16, "tthe" : 0.16, "dthe" : 0.15, "ingt" : 0.15, "ethe" : 0.15, "sand" : 0.14, "sthe" : 0.14, "here" : 0.13, "thec" : 0.13, "ment" : 0.12, "them" : 0.12, "rthe" : 0.12, "thep" : 0.11, "from" : 0.10, "this" : 0.10, "ting" : 0.10, "thei" : 0.10, "ngth" : 0.10, "ions" : 0.10, "andt" : 0.10}
corpusMonogramMagnitude = norm(corpusMonograms)
corpusTetragramFitness = 0

# Converts a character into an integer depending on its alphabetical position
def CharacterToInteger(character):
    return conversionDictionary[str(character)]

# Converts a given integer into its character from alphabetical position
def IntegerToCharacter(integer):
    return list(conversionDictionary.keys())[list(conversionDictionary.values()).index(int(integer))]

# When provided with a text, this function will return a list of monogram frequencies
def CalculateMonogramFrequencies(inputText):
    # Splits the text into a list of individual characters
    textList = [*str(inputText)]

    # Creates a list that will store the count for each letter
    frequencyCount = [0] * 26

    # Loops through each character in the text, and calculates the frequency of each letter
    for i in range(len(textList)):
        characterInt = CharacterToInteger(textList[i])
        frequencyCount[characterInt-1] += 1

    # Calculates the frequencies of each letter as a number so that the sum of them is 1
    for i in range(26):
        frequencyCount[i] = frequencyCount[i] / len(textList)

    # Returns the monogram frequencies to the program
    return frequencyCount


def CalculateTetragramFrequencies(inputText):
    # Splits the text into a list of individual characters
    textList = [*inputText]

    # Creates an empty dictionary with all of the tetragram frequncies
    frequencyCount = {"tion" : 0, "nthe" : 0, "ther" : 0, "that" : 0, "ofth" : 0, "fthe" : 0, "thes" : 0, "with" : 0, "inth" : 0, "atio" : 0, "othe" : 0, "tthe" : 0, "dthe" : 0, "ingt" : 0, "ethe" : 0, "sand" : 0, "sthe" : 0, "here" : 0, "thec" : 0, "ment" : 0, "them" : 0, "rthe" : 0, "thep" : 0, "from" : 0, "this" : 0, "ting" : 0, "thei" : 0, "ngth" : 0, "ions" : 0, "andt" : 0}

    # Loops the tetragram detection for each possible tetragram in the text
    for i in range(len(textList) - 3):
        # Finds the tetragram at this index
        tetragram = textList[i] + textList[i+1] + textList[i+2] + textList[i+3]

        # Checks if it is a common tetragram, and if so adds it into the list
        if str(tetragram) in frequencyCount:
            frequencyCount[tetragram] += 1

    # Places the frequencies into a list, so that they can be accessed by index
    frequencyList = list(frequencyCount.values())

    # Calculates the frequency of each tetragram into a percentage     
    for i in range(30):
        frequencyList[i] = (frequencyList[i] / (len(textList)-3)) * 100
            
    # Returns the frequencies as a list, with each index representing the order of the keys in the dictionary of corpusTetragrams
    return frequencyList

# Calculates the fitness of the given monogram frequencies
# Value closer to 1 leads to better fitness
def CalculateMonogramFitness(inputFrequencies):
    global corpusMonograms
    global corpusMonogramMagnitude

    # Calculates the cosine between the 2 monogram frequencies, giving their fitness
    fitnessValue = np.dot(inputFrequencies, corpusMonograms)/(norm(inputFrequencies)*corpusMonogramMagnitude)

    # Returns the monogram fitness
    return float(fitnessValue)

# Calculates the fitness of the given tetragram fitnesses
# Lower negative leads to a better fitness
def CalculateTetragramFitness(inputFrequencies):
    global corpusTetragrams

    # Converts the values of corpus frequencies into a list
    corpusFrequencies = list(corpusTetragrams.values())

    # Sets the current tetragram fitness to 0
    tetragramFitness = 0

    # Calculate the fitness of each tetragram, and sums them together
    for i in range(30):
        tetragramFitness += inputFrequencies[i] * np.log(corpusFrequencies[i])

    return tetragramFitness


# Sets up the value for the fitness of english text
def SetUpEnglishFitness():
    global corpusTetragrams
    global corpusTetragramFitness

    corpusTetragrams = {}

    with open("CorpusFrequencies\corpusQuadgrams.txt") as f:
        for line in f:
            quad, frequency = line.split(",")
            corpusTetragrams[quad] = float(frequency)

    corpusList = list(corpusTetragrams.values())

    for i in range(len(corpusTetragrams)):
        corpusTetragramFitness += corpusList[i]


    corpusTetragramFitness = float(corpusTetragramFitness / len(corpusTetragrams))

    print(corpusTetragramFitness, "english")

def FindFitness(inputText):
    global corpusTetragrams
    global corpusTetragramFitness

    # Generate all possible four-letter combinations
    allQuadgrams = [inputText[idx:idx+4] for idx in range(len(inputText)-3)]

    # Initialize a variable to store the sum of quadgram frequencies
    totalQuadgramFrequency = 0
    
    # Iterate over each quadgram in the text
    for quadgram in allQuadgrams:
        # Look up the quadgram in the dictionary and add its frequency to the total
        totalQuadgramFrequency += corpusTetragrams.get(quadgram.upper(), 0)

    print(totalQuadgramFrequency, "given total")

    # Calculate the average quadgram frequency and return its absolute value
    quadgramFitness = abs((totalQuadgramFrequency) / len(allQuadgrams))

    print(quadgramFitness, "given average abs")
    print(abs(quadgramFitness - corpusTetragramFitness) / quadgramFitness, "normalised average")


    return abs(quadgramFitness - corpusTetragramFitness) / quadgramFitness

SetUpEnglishFitness()

def FindMonogramFitness(inputText):
    global corpusMonograms

    # Splits the text into a list of individual characters
    textList = [*str(inputText)]

    # Creates a list that will store the count for each letter
    frequencyCount = [0] * 26

    # Declares a variable for the fitness value of the text
    fitnessValue = 0

    # Loops through each character in the text, and calculates the frequency of each letter
    for i in range(len(textList)):
        characterInt = CharacterToInteger(textList[i])
        frequencyCount[characterInt-1] += 1

    # Calculates the frequencies of each letter as a number so that the sum of them is 1
    for i in range(26):
        frequencyCount[i] = frequencyCount[i] / len(textList)

    # Finds the scalar fitness value for the text
    for i in range(26):
        fitnessValue += corpusMonograms[i] - frequencyCount[i]

    return fitnessValue

def FindBigramFitness(inputText):
    global corpusBigrams

    # Converts the corpus values for bigrams into a list
    corpusBigramValues = list(corpusBigrams.values())

    # Splits the text into a list of individual characters
    textList = [*inputText]

    # Empty dictionary with all bigrams tested for
    frequencyCount = {"TH" : 0, "HE" : 0, "IN" : 0, "ER" : 0, "AN" : 0, "RE" : 0, "ES" : 0, "ON" : 0, "ST" : 0, "NT" : 0, "EN" : 0, "AT" : 0, "ED" : 0, "ND" : 0, "TO" : 0, "OR" : 0, "EA" : 0, "TI" : 0, "AR" : 0, "TE" : 0, "NG" : 0, "AL" : 0, "IT" : 0, "AS" : 0, "IS" : 0, "HA" : 0, "ET" : 0, "SE" : 0, "OU" : 0, "OF" : 0}

    # Declares a variable for the scalar fitness value
    fitnessValue = 0

    # Checks if bigram is inside list, and adds it to the dictionary
    for i in range(len(textList) - 1):
        bigram = textList[i] + textList[i+1]

        if(str(bigram).upper() in frequencyCount):
            frequencyCount[bigram.upper()] += 1

    # Converts the values in the dictionary into a list
    frequencyList = list(frequencyCount.values())

    # Converts all of the bigram frequencies into a percentage
    for i in range(len(frequencyCount)):
        frequencyList[i] = (frequencyList[i]/ (len(textList) - 1))

    # Calculates the fitness value of the text
    for i in range(len(frequencyCount)):
        fitnessValue += (corpusBigramValues[i] / 100)- frequencyList[i]

    # Returns the fitness of the text
    return fitnessValue


def FindTrigramFitness(inputText):
    global corpusTrigrams

    corpusTrigramValues = list(corpusTrigrams.values())

    # Splits the text into a list of individual characters
    textList = [*inputText]

    # Empty list with all trigrams being tested for
    frequencyCount = {"THE" :  0, "AND" :  0, "ING" :  0, "ENT" :  0, "ION" :  0, "HER" :  0, "FOR" :  0, "THA" :  0, "NTH" :  0, "INT" :  0, "ERE" :  0, "TIO" :  0, "TER" :  0, "EST" :  0, "ERS" :  0, "ATI" :  0, "HAT" :  0, "ATE" :  0, "ALL" :  0, "ETH" :  0, "HES" :  0, "VER" :  0, "HIS" :  0, "OFT" :  0, "ITH" :  0, "FTH" :  0, "STH" :  0, "OTH" :  0, "RES" :  0, "ONT" :  0}

    # Declares a variable for the scalar fitness value
    fitnessValue = 0

    # Checks if trigram is inside list, and adds it to the dictionary
    for i in range(len(textList) - 2):
        trigram = textList[i] + textList[i+1] + textList[i+2]

        if(str(trigram).upper() in frequencyCount):
            frequencyCount[trigram.upper()] += 1

    # Converts the values in the dictionary into a list
    frequencyList = list(frequencyCount.values())

    # Converts all of the trigram frequencies into a percentage
    for i in range(len(frequencyCount)):
        frequencyList[i] = (frequencyList[i]/ (len(textList) - 1))

    # Calculates the fitness value of the text
    for i in range(len(frequencyCount)):
        fitnessValue += (corpusTrigramValues[i] / 100) - frequencyList[i]
        
    # Returns the fitness of the text
    return fitnessValue

def SearchFitness(inputText):
    monoFitness = 1 - FindMonogramFitness(inputText)
    biFitness = 1 - FindBigramFitness(inputText)
    triFitness = 1 - FindTrigramFitness(inputText)

    fitnessValue = (0.2 * monoFitness) + (0.3 * biFitness) + (0.5 * triFitness)

    return fitnessValue

def AnotherFitnessFunction(inputText):
    monoFitness = 1 - FindMonogramFitness(inputText)
    biFitness = 1 - FindBigramFitness(inputText)

    fitnessValue = (1 - ((monoFitness + biFitness) / 4)) ** 8

    return fitnessValue