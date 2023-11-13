
import CiphertextAnalysis as analysis

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
        plainList.append(keyList[intList[i]])
    
    # Joins up the list of plaintext letters into a word
    decipheredText = "".join(plainList)

    # Returns the deciphered text
    return decipheredText