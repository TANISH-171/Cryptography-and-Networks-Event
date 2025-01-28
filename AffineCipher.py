import string
from math import gcd

def Modular_inverse(num, mod):
    """Find the modular inverse of 'num' under modulo 'mod'."""
    for i in range(mod):
        if (num * i) % mod == 1:
            return i
    return None

def affine_encode(message, key_a, key_b):
    """Encrypt the message using the Affine Cipher."""
    if gcd(key_a, 26) != 1:
        raise ValueError("The key 'key_a' must be coprime with 26.")

    message = message.lower()
    encoded_message = ""
    letters = string.ascii_lowercase

    for char in message:
        if char.isalpha():
            position = letters.index(char)
            encrypted_char = (key_a * position + key_b) % 26
            encoded_message += letters[encrypted_char]
        else:
            encoded_message += char  # Keep non-alphabet characters unchanged

    return encoded_message

def affine_decode(encoded_message, key_a, key_b):
    """Decrypt the encoded message using the Affine Cipher."""
    if gcd(key_a, 26) != 1:
        raise ValueError("The key 'key_a' must be coprime with 26.")

    inverse_a = Modular_inverse(key_a, 26)
    if inverse_a is None:
        raise ValueError("The modular inverse of 'key_a' does not exist.")

    encoded_message = encoded_message.lower()
    decoded_message = ""
    letters = string.ascii_lowercase

    for char in encoded_message:
        if char.isalpha():
            position = letters.index(char)
            decrypted_char = (inverse_a * (position - key_b)) % 26
            decoded_message += letters[decrypted_char]
        else:
            decoded_message += char  # Keep non-alphabet characters unchanged

    return decoded_message

# Example usage
if __name__ == "__main__":
    # User input for message and keys
    original_message = input("Enter the original message: ")
    
    while True:
        try:
            key_a = int(input("Enter key_a (must be coprime with 26): "))
            if gcd(key_a, 26) != 1:
                raise ValueError("Key 'key_a' must be coprime with 26.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    key_b = int(input("Enter key_b: "))

    print("\nOriginal Message:", original_message)

    encrypted_message = affine_encode(original_message, key_a, key_b)
    print("Encoded Message:", encrypted_message)

    decrypted_message = affine_decode(encrypted_message, key_a, key_b)
    print("Decoded Message:", decrypted_message)
