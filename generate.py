import random
import string

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation


def pw_gen():
    security_level = int(input("Choose the security level of your password\n1: password containing only letters\n2: password containing letters and digits\n3: password containing also punctuation\n"))

    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    possible_characters = ""

    if security_level == 1:
        possible_characters += letters

    elif security_level == 2:
        possible_characters += letters + digits

    elif security_level == 3:
        possible_characters += letters + digits + punctuation

    else:
        print("please pick a valid option.")
        pw_gen()


    pw_length = int(input("Choose the length of your password. 8 characters is the minimal length of your password.\n"))

    if pw_length < 8:
        print("The length of your password has been adjusted to the minimum of 8 characters.")
        pw_length = 8

    password = []

    for i in range(pw_length):
        character = random.choice(possible_characters)
        password.append(character)

    password_string = "".join(password)

    print(f"Your randomly generated password with {pw_length} characters is: {password_string}")