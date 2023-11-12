
import CiphertextAnalysis as analysis
import random

# Defines a population, one key that is chosen, and the fitness of that chosen key
population = []
chosenKey = []

# Current generation number
generation = 0

# The starting key for all members and the ciphertext that is being deciphered
masterKey = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
localCiphertext = ""

def BeginDecipher(ciphertext):
    global localCiphertext

    localCiphertext = ciphertext

    InitialisePopulation(10)

    for i in range(400):
        MutatePopulation()
        ChooseKey()

    print(chosenKey)

    print(MonoalphabeticDecipher(localCiphertext, chosenKey))

# Deciphers a text given a key
def MonoalphabeticDecipher(textList, keyList):
    
    # Creates an empty list which describes the ciphertext as integers
    intList = []

    # Converts the list of characters of ciphertext into a list of integers
    for i in range(len(textList)):
        intList.append(analysis.CharacterToInteger(textList[i]))

    # Creates an empty list with all the new text
    plainList = []

    # Substitutes a letter for each of the ciphertext letters
    for i in range(len(intList)):
        plainList.append(keyList[intList[i] - 1])
    
    # Joins up the list of plaintext letters into a word
    decipheredText = "".join(plainList)

    # Returns the deciphered text
    return decipheredText


# Makes a random switch in the key
def RandomKeySwitch(currentKey):

    newKey = list(currentKey)

    # Chooses 2 random keys to swap
    index1 = random.randint(0, 25)
    index2 = random.randint(0, 25)

    # Archives one of the elements, so that it is preserved for the switch
    index1Archive = newKey[index1]

    # Swaps around the keys
    newKey[index1] = newKey[index2]
    newKey[index2] = index1Archive

    # Returns the new key
    return newKey

# Initialises a list with all of the initial keys, with length populationSize
def InitialisePopulation(populationSize):
    global population
    global masterKey
    global chosenKey

    chosenKey = list(masterKey)

    population.append(list(masterKey))

    for i in range(populationSize - 1):
        for i in range(100):
            masterKey = RandomKeySwitch(masterKey)

        population.append(list(RandomKeySwitch(masterKey)))


def MutatePopulation():
    global chosenKey
    global population
    global masterKey

    # Declares a new, empty population
    newPopulation = []

    # Adds at least one uneffected copy of the chosen key
    newPopulation.append(list(chosenKey))

    # Mutates all other keys for the length of the population
    for i in range(len(population) - 1):
        newPopulation.append(RandomKeySwitch(list(chosenKey)))

    # Sets the current population as the new population
    population = list(newPopulation)

def ChooseKey():
    global population
    global chosenKey
    global otherKey

    # Sets up variables to hold the highest fitness key in the population
    highestFitness = -10
    highsetKey = masterKey

    # Finds the highest fitness key from the population
    for i in range(len(population)):

        # Finds the fitness for the key

        currentFitness = analysis.SearchFitness(MonoalphabeticDecipher(localCiphertext, population[i]))
        # currentFitness = analysis.FindFitness(MonoalphabeticDecipher(localCiphertext, population[i]))
        # currentFitness = analysis.AnotherFitnessFunction(MonoalphabeticDecipher(localCiphertext, population[i]))

        print(highestFitness)

        # Checks if the text has a higher fitness than the previous fitness, and updates if neeeded
        if(currentFitness >= highestFitness):
            highestFitness = currentFitness
            highsetKey = list(population[i])

    # Sets the chosen key to the highest key form the generation
    chosenKey = highsetKey


