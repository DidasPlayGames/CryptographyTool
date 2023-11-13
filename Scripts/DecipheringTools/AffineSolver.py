
import CiphertextAnalysis as analysis

localCiphertext = ""

def BeginDecipher(ciphertext):
    global localCiphertext

    localCiphertext = ciphertext

    # Declares variables for the highest fitness combination
    highestFitness = 0
    highestA = 0
    highestB = 0

    # Runs for every value of a apart from 13
    for i in range(1, 27, 2):
        if(i != 13):

            # Runs for every value of b, and checks if there is an increase in performance
            for j in range(26):
                currentFitness = analysis.FindFitness(AffineShift(str(localCiphertext), i, j))

                if(currentFitness > highestFitness):
                    highestFitness = currentFitness
                    highestA = int(i)
                    highestB = int(j)

    print(AffineShift(localCiphertext, highestA, highestB))

# Complete the affine shift for given values of a and b
def AffineShift(inputText, a, b):

    # Declares lists of the text as integers, and the plaintext generated
    intList = []
    newText = []

    # Converts the ciphertext into integers
    for i in range(len(inputText)):
        intList.append(analysis.CharacterToInteger(inputText[i]))

    # Shifts the integers according to the cipher
    for i in range(len(intList)):
        intList[i] = int((((a * intList[i]) + b) % 26))
    
    # Converts the integers back into letters
    for i in range(len(intList)):
        newText.append(analysis.IntegerToCharacter(intList[i]))
    
    # Joins the list back into a word
    newText = "".join(newText)

    return newText