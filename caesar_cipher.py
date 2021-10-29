"""
    Author: Lori White
    Purpose: Showing how to use the caesar cipher in python.
"""
def getMessage():
    """
     Gets the message from the user that is going to be encrypted.
    """
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

def getCipherKey():
    """
     Gets the cipher key for the cipher.
    """
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    """
     Encrypts the message with the cipherKey.
    """
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if newPosition >= len(alphabet):
            newPosition %= len(alphabet)
            
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    """
     Decrypts the message with the cipherKey.
    """
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

def runCaesarCipherProgram():
    """
     Runs the Cipher program.
    """
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet)
    print(f'Decypted Message: {myDecryptedMessage}')

# Main Program code
runCaesarCipherProgram()