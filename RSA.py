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

# Simple RSA key generation
def generate_keys(p, q):
    # Step 1: Compute n = p * q
    n = p * q

    # Step 2: Compute Euler's Totient function phi(n) = (p-1)*(q-1)
    phi_n = (p - 1) * (q - 1)

    # Step 3: Choose e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = 17  # e is typically chosen as 17 or other values
    while gcd(e, phi_n) != 1:
        e += 1

    # Step 4: Compute d such that d * e ≡ 1 (mod phi(n))
    d = mod_inverse(e, phi_n)

    # Return public and private keys
    return (e, n), (d, n)

# Simple encryption function
def encrypt(public_key, message):
    e, n = public_key
    # Encrypt each character of the message
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Simple decryption function
def decrypt(private_key, encrypted_message):
    d, n = private_key
    # Decrypt each character in the encrypted message
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Main function to interact with the user
def rsa_interactive():
    print("Welcome to the Simple RSA Algorithm!")

    # User input for primes p and q
    p = int(input("Enter the first prime number (p): "))
    q = int(input("Enter the second prime number (q): "))

    # Generate RSA keys
    public_key, private_key = generate_keys(p, q)
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    # Input message to encrypt
    message = input("Enter a message to encrypt: ")

    # Encrypt the message
    encrypted_message = encrypt(public_key, message)
    print(f"Encrypted message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = decrypt(private_key, encrypted_message)
    print(f"Decrypted message: {decrypted_message}")

# Run the interactive function
rsa_interactive()
