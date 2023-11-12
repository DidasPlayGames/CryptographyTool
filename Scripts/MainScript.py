import re

import CiphertextAnalysis as analysis
import MonoalphabeticSubstitution as monoalphabetic

import MonoSolver as mono

# Load in the ciphertext from the file
ciphertext = str(open('InputAndOutputTexts\ciphertext.txt', encoding="utf-8").read())

# Formats the ciphertext so that only the text remains
def FormatCiphertext():
    global ciphertext

    # Removes any spaces within the text, and converts it all into lowercase
    ciphertext = ciphertext.replace(" ", "")
    ciphertext = ciphertext.lower()

    # Removes any special character from the text, and keeps only the text
    ciphertext = re.sub('[\W\d_]+', '', ciphertext)

FormatCiphertext()

# monoalphabetic.BreakMonoalphabeticSubstitution(ciphertext)

# print(analysis.FindFitness(ciphertext))

mono.BeginDecipher(ciphertext)
