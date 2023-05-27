def playfair_cipher(text, key):
    key = key.replace(" ", "").lower().replace("j", "i") #Remove spaces and convert to lowercase and replace j with i in key
    key = "".join(dict.fromkeys(key + "abcdefghiklmnopqrstuvwxyz")) #Convert key to dictionary and add all letters in key
    matrix = [key[i:i+5] for i in range(0, 25, 5)] #Create 5x5 matrix from key 
    text = text.replace(" ", "").lower().replace("j", "i") #Remove spaces and convert to lowercase and replace j with i in text
    text += "x" * (len(text) % 2) #Add x to the end of text if it is not even 
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    ciphertext = ""
    for pair in pairs:
        a, b = pair #Split pairs
        a_row, a_col = divmod(key.index(a), 5) #Calculate row and column of a and b 
        b_row, b_col = divmod(key.index(b), 5) #Calculate row and column of a and b
        if a_row == b_row:
                a_col, b_col = (a_col+1)%5, (b_col+1)%5 #If row of a and b are same then change column to next 
        elif a_col == b_col:
                a_row, b_row = (a_row+1)%5, (b_row+1)%5 #If column of a and b are same then change row to next
        else:
            a_col, b_col = b_col, a_col #If column of a and b are not same then swap
        ciphertext += key[a_row*5+a_col] + key[b_row*5+b_col] 
    return ciphertext

def main():
    Plaintext = input("Enter Plaintext: ") #Take Plaintext input from user
    Key = input("Enter Key: ") #Take Key input from user
    Ciphertext = playfair_cipher(Plaintext, Key) #Call playfair_cipher function
    print(f"Plaintext : {Plaintext}\nCiphertext:{Ciphertext}") #Print Plaintext and Ciphertext


main()