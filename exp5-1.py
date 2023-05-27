from Crypto.Cipher import DES
import secrets 

key = secrets.token_bytes(8) #Generate 8 bytes key

# plaintext message to be encrypted
plaintext = b'This is a secret message'

# initialize the DES cipher object
cipher = DES.new(key, DES.MODE_ECB)

# pad the plaintext to be a multiple of 8 bytes
plaintext_padded = plaintext + (b'\0' * (8 - len(plaintext) % 8))

# encrypt the message
ciphertext = cipher.encrypt(plaintext_padded)

# encode the encrypted message in UTF-8 format
encrypted_message = ciphertext.hex().encode('utf-8')

# decrypt the message
decrypted_plaintext_padded = cipher.decrypt(ciphertext)

# remove the padding to get the original plaintext message
decrypted_plaintext = decrypted_plaintext_padded.rstrip(b'\0')

print("Original message:", plaintext)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_plaintext)
