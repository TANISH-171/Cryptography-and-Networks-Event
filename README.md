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

