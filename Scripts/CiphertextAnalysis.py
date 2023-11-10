


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from numpy.linalg import norm


# Establish a global dictionary for the integer equivalent of a character, and frequency analysis
# Monogram values are held as decimal, meanwhile tetragrams are held as a percentage
conversionDictionary = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
corpusMonograms = [0.0855, 0.0160, 0.0316, 0.0387, 0.1210, 0.0218, 0.0209, 0.0496, 0.0733, 0.0022, 0.0081, 0.0421, 0.0253, 0.0717, 0.0747, 0.0207, 0.0010, 0.0633, 0.0673, 0.0894, 0.0268, 0.0106, 0.0183, 0.0019, 0.0172, 0.0011]
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

    corpusTetragramFitness = {}

    with open("CorpusFrequencies\corpusQuadgrams.txt") as f:
        for line in f:
            quad, frequency = line.split(",")
            corpusTetragramFitness[quad] = float(frequency)


def FindFitness(inputText):
    global corpusTetragramFitness

    # Generate all possible four-letter combinations
    allQuadgrams = [inputText[idx:idx+4] for idx in range(len(inputText)-3)]

    # Initialize a variable to store the sum of quadgram frequencies
    totalQuadgramFrequency = 0
    
    # Iterate over each quadgram in the text
    for quadgram in allQuadgrams:
        # Look up the quadgram in the dictionary and add its frequency to the total
        totalQuadgramFrequency += corpusTetragramFitness.get(quadgram.upper(), 0)

    # Calculate the average quadgram frequency and return its absolute value
    return (abs(totalQuadgramFrequency) / len(allQuadgrams))

SetUpEnglishFitness()

# # Calculates the fitness of a given text
# def FindFitness(inputText):
#     global corpusTetragramFitness

#     inputTetragramFrequencies = list(CalculateTetragramFrequencies(inputText))

#     inputFitness = 0

#     for i in range(30):
#         inputFitness += np.log(inputTetragramFrequencies[i])

#     inputFitness = float(np.abs(inputFitness - corpusTetragramFitness) / inputFitness)

#     # Initialize a variable to store the sum of quadgram frequencies
#     total_frequency = 0
    
#     # Iterate over each quadgram in the text
#     for quad in quadtext:
#         # Look up the quadgram in the dictionary and add its frequency to the total
#         total_frequency += quaddict.get(quad.upper(), 0)

#     return inputFitness

# plt.bar(conversionDictionary.keys(), frequencies)
# plt.show()