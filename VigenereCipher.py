import string

def vigenere_encode(message, passkey):
    """
    Encrypt the given message using the Vigenère Cipher algorithm.
    """
    alphabet = string.ascii_lowercase
    message = message.lower()
    passkey = passkey.lower()
    encoded_message = ""
    key_length = len(passkey)

    for index, character in enumerate(message):
        if character.isalpha():
            msg_index = alphabet.index(character)
            key_index = alphabet.index(passkey[index % key_length])
            new_index = (msg_index + key_index) % 26
            encoded_message += alphabet[new_index]
        else:
            encoded_message += character  # Preserve non-alphabetic characters

    return encoded_message


def vigenere_decode(encoded_message, passkey):
    """
    Decrypt the encoded message using the Vigenère Cipher algorithm.
    """
    alphabet = string.ascii_lowercase
    encoded_message = encoded_message.lower()
    passkey = passkey.lower()
    decoded_message = ""
    key_length = len(passkey)

    for index, character in enumerate(encoded_message):
        if character.isalpha():
            enc_index = alphabet.index(character)
            key_index = alphabet.index(passkey[index % key_length])
            original_index = (enc_index - key_index) % 26
            decoded_message += alphabet[original_index]
        else:
            decoded_message += character  # Preserve non-alphabetic characters

    return decoded_message


# Interactive Usage
if __name__ == "__main__":
    print("Vigenère Cipher Program")

    user_message = input("Enter the text to encrypt or decrypt: ")
    user_passkey = input("Enter the keyword for the cipher: ")

    # Encryption
    encrypted_output = vigenere_encode(user_message, user_passkey)
    print("Encrypted Output:", encrypted_output)

    # Decryption
    decrypted_output = vigenere_decode(encrypted_output, user_passkey)
    print("Decrypted Output:", decrypted_output)
