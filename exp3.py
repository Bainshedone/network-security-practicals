def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65) #Shift uppercase characters by amount specified by shift variable
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97) #Shift lowercase characters by amount specified by shift variable
        else:
            result += char
    return result
def main():
    text = input("Enter text to encrypt: ") #Take text input from user
    shift = int(input("Enter shift amount: ")) #Take shift number input from user
    encrypted_text = caesar_cipher(text, shift) #Call caesar_cipher function
    print("Encrypted text:", encrypted_text)


if __name__ == "__main__":
    main()