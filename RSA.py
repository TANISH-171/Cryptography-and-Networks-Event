import random
from sympy import isprime

# Function to generate a prime number within a given range
def generate_prime(start, end):
    prime = random.randint(start, end)
    while not isprime(prime):
        prime = random.randint(start, end)
    return prime

# Function to compute the greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute modular inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Function to generate RSA keys
def generate_rsa_keys():
    print("Generating RSA keys...")
    
    # Step 1: Generate two large prime numbers p and q
    p = generate_prime(100, 200)
    q = generate_prime(100, 200)
    
    # Step 2: Compute n = p * q
    n = p * q
    
    # Step 3: Compute Euler's totient function phi(n) = (p-1)*(q-1)
    phi_n = (p - 1) * (q - 1)
    
    # Step 4: Choose e (public exponent), it should be coprime with phi(n)
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    
    # Step 5: Compute d (private exponent), d is the modular inverse of e modulo phi(n)
    d = mod_inverse(e, phi_n)
    
    # Public key (e, n) and private key (d, n)
    public_key = (e, n)
    private_key = (d, n)
    
    print(f"Generated primes p = {p}, q = {q}")
    print(f"Public key: {public_key}")
    print(f"Private key: {private_key}")
    
    return public_key, private_key

# Function to encrypt a message using the public key
def encrypt(public_key, message):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Function to decrypt a message using the private key
def decrypt(private_key, encrypted_message):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Main function to interact with the user
def rsa_interactive():
    print("Welcome to the RSA Algorithm Interactive Python Program!")
    
    # Generate RSA keys
    public_key, private_key = generate_rsa_keys()
    
    # Ask the user to input a message
    message = input("Enter the message to encrypt: ")
    
    # Encrypt the message using the public key
    encrypted_message = encrypt(public_key, message)
    print(f"Encrypted message (ciphertext): {encrypted_message}")
    
    # Decrypt the message using the private key
    decrypted_message = decrypt(private_key, encrypted_message)
    print(f"Decrypted message: {decrypted_message}")
    
# Run the interactive function
rsa_interactive()
