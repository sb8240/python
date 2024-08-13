import string
import random

char = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("Enter how long you want your password to be: "))
    
    random.shuffle(char)

    password = []

    for x in range(password_length):
        password.append(random.choice(char))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Enter yes/no for if you want to generate a password or not respectively: ")
while True:

    if option == "yes":
        generate_password()
        quit()

    elif option == "no":
        quit()

    else:
        print("Invalid input! pls type yes or no.")



