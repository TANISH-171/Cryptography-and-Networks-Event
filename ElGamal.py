import random

def key_generation(prime):
    """
    Generate public and private keys for the ElGamal cryptosystem with a small prime.
    """
    private_key = random.randint(2, prime - 2)  # Random private key
    generator = random.randint(2, prime - 1)  # Small generator
    public_key = pow(generator, private_key, prime)  # g^private_key mod prime

    return (prime, generator, public_key), private_key  # Public key and private key


def simple_encrypt(message, public_key):
    """
    Encrypt a message using the ElGamal cryptosystem with simple keys.
    """
    prime, generator, shared_key = public_key
    session_key = random.randint(2, prime - 2)  # Random session key
    ephemeral_key = pow(generator, session_key, prime)  # g^session_key mod prime
    shared_secret = pow(shared_key, session_key, prime)  # (pk^session_key mod prime)

    encrypted_message = [(ord(char) * shared_secret) % prime for char in message]

    return ephemeral_key, encrypted_message


def simple_decrypt(encrypted_data, private_key, prime):
    """
    Decrypt an encrypted message using the ElGamal cryptosystem with simple keys.
    """
    ephemeral_key, encrypted_message = encrypted_data
    shared_secret = pow(ephemeral_key, private_key, prime)  # (g^session_key)^private_key mod prime
    inverse_secret = pow(shared_secret, -1, prime)  # Modular inverse of shared secret

    decrypted_message = ''.join([chr((char * inverse_secret) % prime) for char in encrypted_message])

    return decrypted_message


# Example usage
if __name__ == "__main__":
    print("Simple ElGamal Cryptosystem")

    # Small prime number for simplicity
    prime_number = 131  # Small prime
    public_key, private_key = key_generation(prime_number)

    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # Encrypt a simple message
    message_to_encrypt = input("Enter a message to encrypt: ")
    encrypted_data = simple_encrypt(message_to_encrypt, public_key)
    print("Encrypted Data:", encrypted_data)

    # Decrypt the encrypted message
    decrypted_message = simple_decrypt(encrypted_data, private_key, prime_number)
    print("Decrypted Message:", decrypted_message)
