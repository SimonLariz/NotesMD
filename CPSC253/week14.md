## Chapter 21 

## SHA Encryption
- SHA (Secure Hash Algorithm) is a cryptographic hash function that takes an input and produces a fixed-size string of bytes.
- Different versions of SHA are available, such as SHA-1, SHA-256, SHA-384, and SHA-512.

## Message Digest Generation
- Step 1: Append padding bits
- Step 2: Append length
- Step 3: Initialize hash buffer
- Step 4: Process message in blocks
- Step 5: Output hash value

## RSA Public-key Encryption
- RSA (Rivest-Shamir-Adleman) is a public-key cryptosystem that is widely used for secure data transmission.
- Best known and widely used public key algorithm.

## RSA Example
P = 5 Q = 11 
N = P * Q = 55
Q = (P-1) * (Q-1) = 40
E = 3
Message(M) = 7 

Ciphertext(C) = M^E mod N = 7^3 mod 55 = 13 
D = E^-1 mod Q = 3^-1 mod 40 = 27
N = 55
Decrypted Message = C^D mod N = 13^27 mod 55 = 7

# Example 2
P = 23 
Q = 41
N = P * Q = 943
Q = (P-1) * (Q-1) = 880
E = 7 
Message(M) = 35 
C = M^E mod N = 35^7 mod 943 = 545
D = E^-1 mod Q = 7^-1 mod 880 = 503

## Security of RSA
- Brute force attack: trying all possible keys until the correct key is found.
- Mathematical attacks: exploiting the properties of the RSA algorithm to derive the private key from the public key.
- Timing attacks: measuring the time taken to perform cryptographic operations to infer information about the key.
- Chosen-ciphertext attacks: using the ability to decrypt chosen ciphertexts to derive information about the key.

## Timing Attack Countermeasures
- Constant Exponentiation Time: Ensure that the time taken to perform cryptographic operations is constant, regardless of the input.
- Random Delay: Introduce random delays in the cryptographic operations to prevent attackers from inferring information based on timing.
- Blinding - Multiply the ciphertext by a random value before decryption and divide by the same value after decryption to prevent timing attacks.