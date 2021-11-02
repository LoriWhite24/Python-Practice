"""
    Module Lab 6: Caesar Cipher Program Solution
"""

def get_double_alphabet(alphabet):
    """
     Double the given alphabet.
    """
    double_alphabet = alphabet + alphabet
    return double_alphabet

def get_message():
    """
     Get a message to encrypt.
    """
    string_to_encrypt = input("Please enter a message to encrypt: ")
    return string_to_encrypt

def get_cipher_key():
    """
     Get a cipher key.
    """
    # Fixed bug number 1 option 1; by implementing the int() function
    shift_amount = int(input("Please enter a key (whole number from 1-25): "))
    return shift_amount

def encrypt_message(message, cipher_key, alphabet):
    """
     Encrypt Message
    """
    encrypted_message = ""
    uppercase_message = ""
    # Fixed bug number 2 by implementing the upper() function
    uppercase_message = message.upper()
    for current_character in uppercase_message:
        position = alphabet.find(current_character)
        # Fixed bug number 1 option 2; by implementing the int() function
        new_position = position + cipher_key
        if current_character in alphabet:
            encrypted_message = encrypted_message + alphabet[new_position]
        else:
            encrypted_message = encrypted_message + current_character
    return encrypted_message

def decrypt_message(message, cipher_key, alphabet):
    """
     Decrypt Message
    """
    decrypt_key = -1 * int(cipher_key)
    # Fixed bug number 3 by passing the decryptKey as the cipherKey into
    # the encryptMessage() function
    return encrypt_message(message, decrypt_key, alphabet)

def run_caesar_cipher_program():
    """
     Main program logic.
    """
    my_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {my_alphabet}')
    my_alphabet2 = get_double_alphabet(my_alphabet)
    print(f'Alphabet2: {my_alphabet2}')
    my_message = get_message()
    print(my_message)
    my_cipher_key = get_cipher_key()
    print(my_cipher_key)
    my_encrypted_message = encrypt_message(my_message, my_cipher_key, my_alphabet2)
    print(f'Encrypted Message: {my_encrypted_message}')
    my_decrypted_message = decrypt_message(my_encrypted_message, my_cipher_key, my_alphabet2)
    # Fixed bug number 4 by using the proper variable in the print statement below
    print(f'Decrypted Messgae: {my_decrypted_message}')

# Main Logic
run_caesar_cipher_program()
