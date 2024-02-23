# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 2024

@author: adhistark
"""
#variable declarations
text = ''
custom_key = ''

#asking user to input text and key fr vignere cipher
text = input("Enter your text:")
custom_key = input("Enter the key:")

#changing key to lowercase and stripping spaces
custom_key = custom_key.replace(" ","").lower()

# function for vigenere cipher that takes 3 parameters.
# direction defines if it's encryption or decryption
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

#for simplifying function calls
def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

# calls to verify the cipher
encryption = encrypt(text, custom_key)
print(f'\nEncrypted text: {encryption}')
print(f'Key: {custom_key}')
decryption = decrypt(encryption, custom_key)
print(f'\nDecrypted text: {decryption}\n')
print("Is decrypted text same as entered text:", text == decryption)
