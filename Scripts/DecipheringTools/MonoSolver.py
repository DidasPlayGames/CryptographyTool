
import CiphertextAnalysis as analysis
import random
import MonoalphabeticTools as monoTools

# Defines a population, one key that is chosen, and the fitness of that chosen key
population = []
chosenKey = []

# Current generation number
generation = 0

# The starting key for all members and the ciphertext that is being deciphered
masterKey = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
localCiphertext = ""

# This function is called to begin the decipher of a text
# Recommended values are popSize = 5 and genNum = 300
def BeginDecipher(ciphertext, populationSize, generationNum):
    global localCiphertext
    global population
    global chosenKey
    global masterKey

    # Sets up a local variable for the provided ciphertext
    localCiphertext = ciphertext

    # Intialises a population of a set size
    InitialisePopulation(populationSize)

    # Iterates the seleciton process for the number of desired generations
    for i in range(generationNum):
        MutatePopulation()
        ChooseKey()

    # If the key provided produces correct text, print the text and key, and restart the program otherwise
    if(analysis.FindFitness(monoTools.MonoalphabeticDecipher(localCiphertext, chosenKey)) <= 0.99):
        masterKey = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        population = []
        chosenKey = []
        BeginDecipher(localCiphertext)
    else:
        print(chosenKey)
        print(monoTools.MonoalphabeticDecipher(localCiphertext, chosenKey))

# Makes a random switch in the key
def RandomKeySwitch(currentKey):

    # Creates the new key as a copy of the current key 
    newKey = list(currentKey)

    # Chooses 2 random keys to swap
    index1 = random.randint(0, len(currentKey) - 1)
    index2 = random.randint(0, len(currentKey) - 1)

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
        currentFitness = analysis.FindFitness(monoTools.MonoalphabeticDecipher(localCiphertext, population[i]))

        print(highestFitness)

        # Checks if the text has a higher fitness than the previous fitness, and updates if neeeded
        if(currentFitness >= highestFitness):
            highestFitness = currentFitness
            highsetKey = list(population[i])

    # Sets the chosen key to the highest key form the generation
    chosenKey = highsetKey


