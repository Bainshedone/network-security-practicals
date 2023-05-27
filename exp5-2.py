import random
import math

def generate_keypair(p: int, q: int): # p and q are prime numbers
    n = p * q # first part of public key
    phi = (p-1) * (q-1) #calculate phi it's a part of private key
    e = random.randrange(1, phi) #public key exponent
    g = math.gcd(e, phi) #gcd (greatest common divisor)
    while g != 1:
        e = random.randrange(1, phi) 
        g = math.gcd(e, phi)
    d = pow(e, -1, phi) #private key exponent
    return (e, n), (d, n) #return public and private key

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [(ord(char) ** e) % n for char in plaintext] #Encrypt plaintext using public key
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = [chr((char ** d) % n) for char in ciphertext] #Decrypt ciphertext using private key
    return ''.join(plaintext)


def main():
    p = int(input("Enter p: "))
    q = int(input("Enter q: "))
    public, private = generate_keypair(p, q)
    print(f"Public key: {public}")
    print(f"Private key: {private}")
    message = input("Enter message: ")
    print(f"Plaintext: {message}")
    ciphertext = encrypt(public, message)
    print(f"Ciphertext: {ciphertext}")
    decryptedtext = decrypt(private, ciphertext)
    print(f"decrypted text: {decryptedtext}")



main()