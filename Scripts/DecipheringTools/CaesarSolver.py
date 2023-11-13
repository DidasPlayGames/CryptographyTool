
import CiphertextAnalysis as analysis

localCiphertext = ""

# This function is called to begin the deciphering
def BeginDecipher(ciphertext):
    global localCiphertext

    # Creates a local copy for the ciphertext
    localCiphertext = ciphertext

    # Declares the variable for the currently highest fit, and the shift required for it
    highestFitness = 0
    bestShift = 0

    # Iterates through all shifts, and finds the shift that fits the most
    for i in range(26):
        currentFitness = analysis.FindFitness(ShiftText(localCiphertext, i))

        if(currentFitness > highestFitness):
            highestFitness = currentFitness
            bestShift = i

    # The deciphered text is outputted
    print(ShiftText(localCiphertext, bestShift))



def ShiftText(inputText, shiftAmount):

    # Declares 2 lists, one with the string as an integer, and one with the new plaintext
    intList = []
    newText = []

    # Converts the entire string into numbers
    for i in range(len(inputText)):
        intList.append(analysis.CharacterToInteger(inputText[i]))

    # Shifts each letter
    for i in range(len(intList)):
        intList[i] = int(((intList[i] + shiftAmount) % 26))

    # Converts the shifted integer list back into text
    for i in range(len(intList)):
        newText.append(analysis.IntegerToCharacter(intList[i]))

    # Joins the list of letters together
    newText = "".join(newText)

    # Returns the string
    return str(newText)