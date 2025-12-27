import string
import sys

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

def pw_check():
    your_password = str(input("Please enter the password that you want to check for its security level.\n"))

    

    if len(your_password) < 8:
        base_security = 0
        print("It is recommended that your password has at least 8 characters.")
    else: 
        base_security = (len(your_password) -4) // 4 # base_security starts at 1 for a pw of length 8 and increases by 1 for every 4 characters.

    if base_security > 4:
        base_security = 4

    lower = 0
    upper = 0
    digit = 0
    punct = 0

    for char in your_password:
        if char in lowercase:
            lower = 1
        if char in uppercase:
            upper = 1
        if char in digits:
            digit = 1
        if char in punctuation:
            punct = 1

    security = base_security + lower + upper + digit + punct

    print(f"The security level of '{your_password}' is {security} out of 8.")
    if security < 8:
        print("You can improve the security of your password by:")
        if base_security < 4:
            print("- choosing a longer password.")
        if lower == 0:
            print("- adding lowercase letters to your password.")
        if upper == 0:
            print("- adding uppercase letters to your password.")
        if digit == 0:
            print("- adding digits to your password.")
        if punct == 0:
            print("- adding punctuation to your password.")

    go_again = int(input("\n\nDo you want to check another password?\n1: Yes\n2: No\n"))

    if go_again == 1:
        print("\n")
        pw_check()
    else:
        sys.exit()

    



