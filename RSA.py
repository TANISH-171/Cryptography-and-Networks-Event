import random
from math import gcd

# Function to calculate the modular multiplicative inverse of a under modulo m
def mod_inverse(a, m):
    """Find modular inverse of a under modulo m."""
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Function to check if a number is prime
def is_prime(n):
    """Check if the number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to generate prime numbers randomly
def generate_prime_number():
    """Generate a random prime number."""
    while True:
        num = random.randint(100,500)
        if is_prime(num):
            return num

# RSA Key Generation
def generate_keys():
    """Generate public and private keys for RSA."""
    p = generate_prime_number()
    q = generate_prime_number()
    while p == q:
        q = generate_prime_number()  # Ensure p and q are different

    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Find e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # Find d such that d * e ≡ 1 (mod phi(n))
    d = mod_inverse(e, phi_n)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

# RSA Encryption
def encrypt(message, public_key):
    """Encrypt the message using RSA encryption."""
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# RSA Decryption
def decrypt(encrypted_message, private_key):
    """Decrypt the encrypted message using RSA decryption."""
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Main interactive function
if __name__ == "__main__":
    print("RSA Cryptosystem")

    # Generate RSA keys
    public_key, private_key = generate_keys()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt(message, public_key)
            print("Encrypted Message:", encrypted_message)

        elif choice == '2':
            encrypted_message = list(map(int, input("Enter the encrypted message (comma-separated): ").split(',')))
            decrypted_message = decrypt(encrypted_message, private_key)
            print("Decrypted Message:", decrypted_message)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select again.")
