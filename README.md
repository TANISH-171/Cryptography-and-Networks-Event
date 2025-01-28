# Cryptography-and-Networks-Event
 
1. Implement Affine Cipher.
2. Implement Vigenere Cipher.
3. Implement Extended Euclidean Algorithm.
4. Implement RSA: Select e, d, n. Encrypt a word using e decrypt using d.
5. Implement El-Gamal: Select e1, e2, r, d. Compute C1,C2(Cipher Texts). Decrypt using d.
__________________________________________________________________________________________
1. Affine Cipher Basics:
   *The cipher uses a mathematical formula:
    Encryption: 𝐸(𝑥)=(𝑎⋅𝑥+𝑏) mod 26
    Decryption: D(x)=a^-1(x-b) mod 26

2. Vigenere Cipher Basics:
   *Takes a plaintext and a keyword as input.
   *Converts both to uppercase for uniformity.
   Encryption: E(Pi)=(Pi+Ki) mod 26
   Decryption: D(Ci)=(Ci−Ki) mod 26

3. Extended Euclidean Algorithm :
   *The Euclidean Algorithm is a method for finding the Greatest Common Divisor (GCD) of two integers. The GCD of two integers is the largest number that divides both of them without leaving a remainder.
   *Given two integers a and b, where 𝑎>𝑏.
   *Divide 𝑎 by 𝑏 and get the remainder 𝑟.
    𝑎 = 𝑏 ⋅ 𝑞 + 𝑟
   *This algorithm gives GCD and Modular Inverse as output.

4. RSA :
   *Key Generation:
    ~Choose two large primes 'p' and 'q'.
    ~Compute n = p x q.
    ~compute 𝜙(𝑛) =(p-1).(q-1).
    ~Choose e such that 1<e<𝜙(𝑛) and e is coprime to 𝜙(𝑛) ie. GCD(e,𝜙(𝑛))=1.
    ~Calculate Private key d = e^-1 mod 𝜙(𝑛)
    ~Public key is (n,e) and Private key is d.

   *Encryption:
    ~the ciphertext 'C' is 
         C = (P^e) mod n
   *Decryption:
    ~the plaintext 'P' is
         P = (C^d) mod n

5. ElGamal Cryptosystem:
   *Key Generation:
    ~Public Parameters: Select a large prime number p and a generator g of the multiplicative group Z*p.
    ~Private Key: Select a private key x such that 1 ≤ x ≤p −2.
    ~Public Key: Compute h=gx mod  p. The public key is (p,g,h) and the private key is x.

   *Encryption:
    ~Choose a random integer k such that 1 ≤ k ≤ p−2.
    ~Compute C1 = g^k mod  p.
    ~Compute C2 =M⋅h^k mod  p.
    ~The ciphertext is (c1,c2).

   *Decryption:
    ~To decrypt the ciphertext (c1,c2) using the private key x:
    ~Compute the shared secret s= Cx1 mod  p.
    ~Compute s−1 mod  p (the modular inverse of s).
    ~Compute the original message M = C2⋅s−1 mod  p.