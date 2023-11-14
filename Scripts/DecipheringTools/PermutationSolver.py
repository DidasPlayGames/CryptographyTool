
import CiphertextAnalysis as analysis

localCiphertext = ""

def BeginDecipher(ciphertext):
    global localCiphertext

    localCiphertext = ciphertext


# This function converts a text into rows of a set length
def ConvertIntoRows(inputText, rowLength):
    # Declares an empty list with all the rows
    rowsList = []

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

    # Returns the list of permutated rows
    return list(permutatedRowsList)