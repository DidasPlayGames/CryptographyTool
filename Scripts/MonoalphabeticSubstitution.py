import CiphertextAnalysis as analysis
import random
import sys

# Sets up the original key and the global ciphertext variable
masterKey = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
localCiphertext = ""

# Sets up a variable for the count of iterations of the program, and the total number of improvements
iterationCount = 0
improvementCount = 0

# Increases the python recursion limit to allow the script to run for longer
sys.setrecursionlimit(10**5)

# This function is called from main script to start this script
def BreakMonoalphabeticSubstitution(givenText):
    global localCiphertext

    # Sets up the given text as the ciphertext that is provided to the script
    localCiphertext = givenText

    # MainLoop(masterKey, analysis.CalculateMonogramFitness(analysis.CalculateMonogramFrequencies(givenText)))
    
    TheMainLoop(masterKey)

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
    newKey = currentKey

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


# The main function in the program, which will be looped to complete the process
def MainLoop(keyNow, fitnessNow):
    global localCiphertext
    global iterationCount
    global count 
    global otherCount

    # Creates a new key and calculates the fitness for it
    archiveKey = list(keyNow)
    archiveFitness = float(fitnessNow)

    newKey = RandomKeySwitch(keyNow)
    newText = str(MonoalphabeticDecipher(localCiphertext, newKey))
    newFitness = analysis.CalculateMonogramFitness(analysis.CalculateMonogramFrequencies(newText))

    # print(fitnessNow)
    # print(archiveFitness)

    print(analysis.CalculateTetragramFitness(analysis.CalculateTetragramFrequencies(str(newText))), "new")
    print(analysis.CalculateTetragramFitness(analysis.CalculateTetragramFrequencies(str(localCiphertext))), "current")

    if(newFitness > archiveFitness):
        if(archiveFitness >= 0.98):
            if(analysis.CalculateTetragramFitness(analysis.CalculateTetragramFrequencies(newText)) - 100 > analysis.CalculateTetragramFitness(analysis.CalculateTetragramFrequencies(localCiphertext))):
                otherCount += 1
                iterationCount = 0
                localCiphertext = newText
                open("InputAndOutputTexts\ciphertext.txt", "w").write(str(localCiphertext))
                MainLoop(newKey, newFitness)
            else:
                if(iterationCount >= 1000):
                    print(MonoalphabeticDecipher(localCiphertext, archiveKey))
                    print(count)
                    print(otherCount)
                else:
                    iterationCount += 1
                    MainLoop(archiveKey, archiveFitness)
        else:
            count += 1
            iterationCount = 0
            localCiphertext = newText
            open("InputAndOutputTexts\ciphertext.txt", "w").write(str(localCiphertext))
            MainLoop(newKey, newFitness)
    else:
        if(iterationCount >= 1000):
            print(MonoalphabeticDecipher(localCiphertext, archiveKey))
            print(count)
            print(otherCount)
        else:
            iterationCount += 1
            MainLoop(archiveKey, archiveFitness)

# Main function of the program, which is looped to improve the function (The Hill Climbing Part)
def NewMainLoop(currentKey, currentFitness):
    global localCiphertext
    global iterationCount
    global improvementCount

    # Generates a new key, decrypts the ciphertext using it, and finds the fitness of that text
    newKey = list(RandomKeySwitch(currentKey))
    newCiphertext = str(MonoalphabeticDecipher(localCiphertext, newKey))
    newFitness = float(analysis.FindFitness(newCiphertext))

    print(currentFitness, "current")
    print(newFitness, "new")

    # Decides if the new text is more fitting than the current text
    if(newFitness > currentFitness):
        # Adds to the improvement counter
        improvementCount += 1

        # Saves the new ciphertext to the file, and modifies the local ciphertext to be the new ciphertext
        open("InputAndOutputTexts\ciphertext.txt", "w").write(str(newCiphertext))
        localCiphertext = newCiphertext

        # Resets the iteration count to 0
        iterationCount = 0

        # Repeats the algorithm with the new key and fitness
        NewMainLoop(newKey, newFitness)
    else:
        # Checks if no improvement has been made for the past 2000 iterations
        if(iterationCount == 2700):
            # Outputs the local ciphertext, and the number of improvements that have been accomplished
            print(localCiphertext)
            print(improvementCount)
        else:
            # Increments the counter of unsuccessful iterations
            iterationCount += 1

            # Repeats the algorithm with the past key and fitness
            NewMainLoop(currentKey, currentFitness)


def TheMainLoop(currentKey):
    global localCiphertext
    global iterationCount
    global improvementCount

    currentText = str(MonoalphabeticDecipher(localCiphertext, currentKey))
    currentFitness = float(analysis.FindFitness(localCiphertext))

    if(iterationCount != 2700):
        newKey = list(RandomKeySwitch(currentKey))
        newCiphertext = str(MonoalphabeticDecipher(currentText, newKey))
        newFitness = float(analysis.FindFitness(newCiphertext))

        print(currentFitness, "current")
        print(newFitness, "new")

        if(newFitness > currentFitness):
            improvementCount += 1

            open("InputAndOutputTexts\ciphertext.txt", "w").write(str(newCiphertext))
            localCiphertext = newCiphertext

            iterationCount = 0

            TheMainLoop(newKey)

        iterationCount += 1

        TheMainLoop(currentKey)
    else:
        print(localCiphertext)
        print(improvementCount)


    
