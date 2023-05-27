def passcheck(password: str):
    if len(password)<8: #Password's min length should be 8
        print("Password must atleast have 8 characters") 
    elif " " in password: #Password cannot contain spaces
        print("Password cannot contain spaces")
    else:
        upper = False 
        lower = False
        digit = False
        special = False
        for char in password:
            if char.isupper(): #Check if password contains uppercase
                upper = True
            elif char.islower(): #Check if password contains lowercase
                lower = True
            elif char.isdigit(): #Check if password contains digit
                digit = True
            elif not char.isalpha(): #Check if password contains special character
                special = True

        passlen = len(password) + upper + lower + digit + special
        percent = passlen * 100 / 12 #Calculate percentage of security based on above parameters
        if percent>100: #If percentage is greater than 100 then it is 100
            percent = 100
        print(f"{percent}% of the password is correct")
        if not (upper and lower and digit and special):
            evalution = "Your password is missing"
            if not upper:
                evalution += " uppercase letter,"
            if not lower:
                evalution += " lowercase letter,"
            if not digit:
                evalution += " digit,"
            if not special:
                evalution += " special character,"
            print(evalution)


def main():
    username = input("Enter Username: ") #Take username input from user
    password = input("Enter Password: ") #Take password input from user
    passcheck(password) #Call passcheck function



if __name__ == "__main__":
    main()














