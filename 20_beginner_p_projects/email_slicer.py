def main():
    print("Welcome to the email slicer\n\n")

    email_input = input("Enter your email address: ")

    (user_name, ini_domain) = email_input.split("@")
    (fin_domain, extension) = ini_domain.split(".")
    
    print("Username : ", user_name )
    print("Doamin : ", fin_domain)
    print("Extension : ", extension)

main() 