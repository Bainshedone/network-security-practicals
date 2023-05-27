import hashlib

input_string = "Hello world" # replace with your input string
hash_object = hashlib.md5(input_string.encode())
md5_hash = hash_object.hexdigest()

print(md5_hash)
