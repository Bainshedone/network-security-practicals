def main():
    username = input("Enter Username: ") #Take username input from user
    password = input("Enter Password: ") #Take password input from user
    if password:
        protected = len(password) * "*" #Convert password to protected password aka into *
        print(f"Username: {username}\nPassword: {protected}\n\n{password}")
    else:
        print("Enter Password")


main()