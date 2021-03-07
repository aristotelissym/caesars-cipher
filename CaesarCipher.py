"""
================================================== Caesars Cipher: =======================================================================
It is the oldest, but the simpliest Replacement Algorithm.
Each letter(character) of the Plain Text is being replaced by a letter(character) which is 3 places in front of it.
Now, the displacement could be random - given by the user or the system -.
The Algorithm that describes the Conversion from the Plain Text to the Cypher Text is: C = E(k,p) = (p + k) mod26.
The Algorithm that describes the Conversion from the Cypher Text to the Plain Text is: P = D(k,p) = (C - k) mod26.
Caesars Cipher, could break with Cryptoanalysis. The most common way is brute-force, if we know:
        1. The Encryption and Decryption Algorithms.
        2. The multitude of the Symmetric Key.
        3. The Natural Language with which the Plain Text was written.

Creator: 
    @aristotelissym, Github Account
    E-mail: arisymeon97@gmail.com
===========================================================================================================================================
"""

"""Alphabet Array"""
alphaArray = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,
              'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, ' ': 26, '!': 27, '@': 28, '#': 29, '$': 30, '%': 31, '^': 32, '&': 33, '*': 34,
              '(': 35, ')': 36, '`': 37, '~': 38, '1': 39, '2': 40, '3': 41}

""" Plain Text Variables"""
plainText = " "
plainStuff = []
plainValues = []

"""Cypher Text Variables"""
cypherText = " "
cypherStuff = []
cypherValues = []


def Programming_Function():
    request = input(
        "This is Caesars Cipher, made with Python.\nIf you wish to Encrypt a message press 1.\nIf you wish to Decrypt a message press 2.\n")
    if (request == "1"):
        print("Please type the message that you want to Cipher: ")
        enc_input = input()
        print("Please type the key with which you will encrypt your message: ")
        key_input = input()

        print(Encryption_Function(str(enc_input), int(key_input)))
    if (request == "2"):
        print("Please type the message that you want to Decipher: ")
        de_input = input()
        print("Please type the key with which you will decrypt your message: ")
        key_input = input()

        print(Decryption_Function(str(de_input), int(key_input)))


# The Function that Encrypts the plainText -> CypherText.
def Encryption_Function(plainText, symmetric_key):
    global cypherText

    # The program reads the plainText each character at a time, and then it matches the characters with each value, and puts all the values into an array.
    for character in range(0, len(plainText)):
        if plainText[character].lower() in alphaArray:
            plainStuff.append(int(alphaArray[plainText[character]]))

        # Then, it reads each value from the plainStuff Array, and computes each variable as:
        # C = E(symmetric_key, array_value) = (array_value + symmetric_key) mod(the crowd of the total characters in alphaArray)
        # Then, each new value goes into a new array(cypherValues).
    for aVar in range(0, len(plainStuff)):
        new_value = plainStuff[aVar] + symmetric_key
        symmetric_value = new_value % 31
        cypherValues.append(symmetric_value)
        symmetric_value = 0

        # In the end, this for-loop, gets each value from the cypherValues Array, and then prints the character that matches the value from the alphaArray.
    for bVar in range(0, len(cypherValues)):
        for key, value in alphaArray.items():
            if cypherValues[bVar] == value:
                cypherText += str(key)
    return (cypherText)


# The Function that Dencrypts the CypherText -> PlainText.
# Has the same explanation as with the Encryption_Function.*
def Decryption_Function(cypherText, symmetric_key):
    global plainText

    for letter in range(0, len(cypherText)):
        if cypherText[letter].lower() in alphaArray:
            cypherStuff.append(int(alphaArray[cypherText[letter]]))

        # *But now, as it reads each value from the CypherStuff Array, it computes each variable as:
        #  P = D(symmetric_key, array_value) = (array_value - symmetric_key) mod(the crowd of the total characters in alphaArray)
    for sth in range(0, len(cypherStuff)):
        new_value = cypherStuff[sth] - symmetric_key
        symmetric_value = new_value % 31
        plainValues.append(symmetric_value)
        symmetric_value = 0

    for var in range(0, len(plainValues)):
        for key, value in alphaArray.items():
            if plainValues[var] == value:
                plainText += str(key)


Programming_Function()  # Runs the Program.
