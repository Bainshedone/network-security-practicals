def encrypt(string):
    new_string = ""
    for char in string:
        if char.isupper():
            new_string += chr((ord(char) + 3 - 65) % 26 + 65) #Shift uppercase characters by +3
        elif char.islower():
            new_string += chr((ord(char) + 3 - 97) % 26 + 97) #Shift lowercase characters by +3
    return new_string

def dencrypt(string):
    new_string = ""
    for char in string:
        if char.isupper():
            new_string += chr((ord(char) - 3 - 65) % 26 + 65) #Shift uppercase characters by -3
        elif char.islower():
            new_string += chr((ord(char) - 3 - 97) % 26 + 97) #Shift lowercase characters by +3
    return new_string


    
def main():
    option = input("Enter 1 to encrypt or 2 to decrypt: ")
    if option == "1":
        string = input("Enter string to encrypt: ") #Take Plain text input from user
        print(encrypt(string)) #Call encrypt function
    elif option == "2":
        string = input("Enter string to decrypt: ") #Take Cipher text input from user
        print(dencrypt(string)) #Call dencrypt function
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
