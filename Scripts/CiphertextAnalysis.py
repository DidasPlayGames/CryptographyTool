
import re

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

# Establish a global dictionary for the integer equivalent of a character
conversionDictionary = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}

# Load in the ciphertext from the file
ciphertext = str(open('InputAndOutputTexts\ciphertext.txt').read())

# Opens both corpus frequency files
fCorpusMonograms = open("CorpusFrequencies\MonogramFrequencies.txt")
fCorpusTetragrams = open("CorpusFrequencies\TetragramFrequencies.txt")

# Creates a list and dictionary for corpus frequencies 
corpusMonograms = [0] * 26
corpusTetragrams = {"" : 0}

# Loads in the monogram frequencies into a list
for i in range(26):
    corpusMonograms[i] = fCorpusMonograms.readline().replace("\n", "")

print(corpusMonograms)

# Converts a character into an integer depending on its alphabetical position
def CharacterToInteger(character):
    return conversionDictionary[str(character)]

# Converts a given integer into its character from alphabetical position
def IntegerToCharacter(integer):
    return list(conversionDictionary.keys())[list(conversionDictionary.values()).index(int(integer))]

# When provided with a text, this function will return a list of monogram frequencies
def CalculateMonogramFrequencies(inputText):
    # Removes any spaces within the text, and converts it all into lowercase
    inputText = inputText.replace(" ", "")
    inputText = inputText.lower()

    # Removes any special character from the text, and keeps only the text
    inputText = re.sub('[\W\d_]+', '', inputText)

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

frequencies = CalculateMonogramFrequencies(ciphertext)


plt.bar(conversionDictionary.keys(), frequencies)
plt.show()



