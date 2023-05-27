import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


# KeySpec interface for AES keys
class AESKeySpec:
    def __init__(self, key):
        self.key = key


# KeyFactory for AES keys
class AESKeyFactory:
    def generate_key(self):
        return AESKeySpec(get_random_bytes(32))


# AES Cipher implementation
class AESCipher:
    def __init__(self, key_spec):
        self.key = key_spec.key
        self.cipher = AES.new(self.key, AES.MODE_CBC)

    # Encrypt a message and return the base64-encoded value
    def encrypt(self, message):
        # Generate a random initialization vector (IV)
        iv = self.cipher.iv
        # Encrypt the message using the AES cipher in CBC mode and pad to block size
        encrypted_message = self.cipher.encrypt(pad(message, AES.block_size))
        # Concatenate the IV and encrypted message, base64-encode, and return
        return base64.b64encode(iv + encrypted_message)

    # Decrypt a message from a base64-encoded value
    def decrypt(self, encrypted_message):
        # Decode the base64-encoded message and extract the IV
        encrypted_message = base64.b64decode(encrypted_message)
        iv = encrypted_message[:AES.block_size]
        # Decrypt the message using the AES cipher in CBC mode and unpad
        cipher_text = encrypted_message[AES.block_size:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_message = unpad(cipher.decrypt(cipher_text), AES.block_size)
        return decrypted_message


# Example usage
key_factory = AESKeyFactory()
key_spec = key_factory.generate_key()
cipher = AESCipher(key_spec)
message = b"Hello, World!"
encrypted_message = cipher.encrypt(message)
print("Encrypted message:", encrypted_message)
decrypted_message = cipher.decrypt(encrypted_message)
print("Decrypted message:", decrypted_message)
