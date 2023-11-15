
import random as r

import CiphertextAnalysis as analysis
import DecipheringTools.MonoSolver as monoalphabetic

localCiphertext = ""

# Declares a variable for the counter, which is used to run the main loop
counter = 0

# Declares variable for master key, which is filled in according to the row length
masterKey = []

# Declares variables for highest fitness and the key for it
chosenKey = []
chosenFitness = 0

# Declares a variable that holds the key length currently being tested
keyLength = 1

def BeginDecipher(ciphertext, inputKeyLength):
    global localCiphertext
    global masterKey
    global chosenKey
    global counter
    global chosenFitness
    global keyLength

    # Copies the provided variable into a global variable
    keyLength = inputKeyLength

    # Copies the provided ciphertext into a local variable
    localCiphertext = ciphertext

    # Intialises both the master and chosen key
    InitialiseMasterKey(keyLength)
    chosenKey = list(masterKey)

    # Runs for a set 
    while counter < (200 * keyLength):
        # Declares a variable for the new ciphertext created, its key, and its fitness
        currentText = ""
        currentKey = []
        currentFitness = 0

        # Runs a random choice to decide what should be done
        if(r.randint(0, 1) == 0):
            # Random switch is done in the key
            currentKey = list(monoalphabetic.RandomKeySwitch(list(chosenKey)))
        else:
            # Chooses a random amount to rotate the key
            rotateAmount = r.randint(1,keyLength)

            # Rotates the list by that set amount
            currentKey = list(RotateList(list(chosenKey), rotateAmount))


        # Finds the ciphertext from the new key
        currentText = CompletePermutation(ConvertIntoRows(localCiphertext, keyLength), list(currentKey))
        currentFitness = analysis.FindFitness(currentText)

        # Choose the new key if its fitness is higher, or if its fitness is higher with margin and 1/20 chance is taken
        if(((currentFitness + 0.025) > chosenFitness and (r.randint(1, 80) == 1) and (chosenFitness < 0.97)) or (currentFitness > chosenFitness)):
            # Copies over the keys and its fitness
            chosenKey = list(currentKey)
            chosenFitness = float(currentFitness)

            # Resets the counter to 0
            counter = 0
        else:
            # Increments the counter
            counter += 1

        # Prints the fitness during each iteration as a display of the algorithm working
        print(currentFitness, "current")
        print(chosenFitness)
    
    # Output the key and plaintext after all of the permutations have been completed
    print(CompletePermutation(ConvertIntoRows(localCiphertext, keyLength), chosenKey))
    print(chosenKey)

# Declares a master key with the length of the row
def InitialiseMasterKey(length):
    global masterKey

    for i in range(length):
        masterKey.append(int(i+1))

# This function converts a text into rows of a set length
def ConvertIntoRows(inputText, rowLength):
    # Declares an empty list with all the rows
    rowsList = []

    # Converts the inputText into a list of characters
    inputText = [*inputText]

    # If the ciphertext is not a multiple of the length of the row, pad it
    if((len(inputText) % rowLength) != 0):
        for i in range(len(inputText) % rowLength):
            inputText.append("x")

    # Loops for the number of rows to be created
    for i in range(int(len(inputText) / rowLength)):
        # Declares an empty variable that stores the row
        row = []
        
        # Adds all of the characters into a row as a list
        for j in range(rowLength):
            row.append(inputText[(5*i) + j])
        
        # Converts the list into a string
        row = str("".join(row))

        # Adds the new row into the list of all rows
        rowsList.append(row)

    # Returns a list of all the rows
    return list(rowsList)

# This function completes a given permutation on each row in the list
def CompletePermutation(rowsList, permutationList):
    # Declares a variable for the new permutated list of rows
    permutatedRowsList = []

    # Loops the permutation for each row in the list
    for i in range(len(rowsList)):
        # Converts the row into individual characters
        row = [*rowsList[i]]

        # Declares a variable for the new permutated row
        permutatedRow = []

        # Completes the permutation for each character in the row
        for j in range(len(permutationList)):

            # Permutates the row
            permutatedRow.append(row[permutationList[j] - 1])

        # Converts the permutated row into a string
        row = str("".join(permutatedRow))

        # Adds the newly permutated row into the list of permutated rows
        permutatedRowsList.append(row)

    # Returns the permutated rows as one string
    return "".join(permutatedRowsList)

# Rotates a list by a set amount
def RotateList(lst, n):
    return list(reversed(lst[-n:])) + lst[:-n]