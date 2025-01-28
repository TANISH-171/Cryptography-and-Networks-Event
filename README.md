# Cryptography-and-Networks-Event
 
1. Implement Affine Cipher.<br />
2. Implement Vigenere Cipher.<br />
3. Implement Extended Euclidean Algorithm.<br />
4. Implement RSA: Select e, d, n. Encrypt a word using e decrypt using d.<br />
5. Implement El-Gamal: Select e1, e2, r, d. Compute C1,C2(Cipher Texts). Decrypt using d.<br />
__________________________________________________________________________________________
**1. Affine Cipher Basics:**<br />
   *The cipher uses a mathematical formula:<br />
    Encryption: 𝐸(𝑥)=(𝑎⋅𝑥+𝑏) mod 26<br />
    Decryption: D(x)=a^-1(x-b) mod 26<br /><br />

**2. Vigenere Cipher Basics:**<br />
   *Takes a plaintext and a keyword as input.<br />
   *Converts both to uppercase for uniformity.<br />
   Encryption: E(Pi)=(Pi+Ki) mod 26<br />
   Decryption: D(Ci)=(Ci−Ki) mod 26<br /><br />

**3. Extended Euclidean Algorithm :**<br />
   *The Euclidean Algorithm is a method for finding the Greatest Common Divisor (GCD) of two integers. The GCD of two integers is the largest number that divides both of them without leaving a remainder.<br />
   *Given two integers a and b, where 𝑎>𝑏.<br />
   *Divide 𝑎 by 𝑏 and get the remainder 𝑟.<br />
    𝑎 = 𝑏 ⋅ 𝑞 + 𝑟<br />
   *This algorithm gives GCD and Modular Inverse as output.<br /><br />

**4. RSA :**
   *Key Generation:<br />
    ~Choose two large primes 'p' and 'q'.<br />
    ~Compute n = p x q.<br />
    ~compute 𝜙(𝑛) =(p-1).(q-1).<br />
    ~Choose e such that 1<e<𝜙(𝑛) and e is coprime to 𝜙(𝑛) ie. GCD(e,𝜙(𝑛))=1.<br />
    ~Calculate Private key d = e^-1 mod 𝜙(𝑛)<br />
    ~Public key is (n,e) and Private key is d.<br />
   *Encryption:<br />
    ~the ciphertext 'C' is <br />
         C = (P^e) mod n<br />
   *Decryption:<br />
    ~the plaintext 'P' is<br />
         P = (C^d) mod n<br /><br />
**5. ElGamal Cryptosystem:**
   *Key Generation:<br />
    ~Public Parameters: Select a large prime number p and a generator g of the multiplicative group Z*p.<br />
    ~Private Key: Select a private key x such that 1 ≤ x ≤p −2.<br />
    ~Public Key: Compute h=gx mod  p. The public key is (p,g,h) and the private key is x.<br />
   *Encryption:<br />
    ~Choose a random integer k such that 1 ≤ k ≤ p−2.<br />
    ~Compute C1 = g^k mod  p.<br />
    ~Compute C2 =M⋅h^k mod  p.<br />
    ~The ciphertext is (c1,c2).<br />
   *Decryption:<br />
    ~To decrypt the ciphertext (c1,c2) using the private key x:<br />
    ~Compute the shared secret s= Cx1 mod  p.<br />
    ~Compute s−1 mod  p (the modular inverse of s).<br />
    ~Compute the original message M = C2⋅s−1 mod  p.<br />
