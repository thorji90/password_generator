import sys
from check import pw_check
from generate import pw_gen

choice = int(input("What do you want to do? Type 1 or 2.\n1: generate a random password\n2: check the security of your password\n"))

if choice == 1:
    pw_gen()
elif choice == 2:
    pw_check()
else:
    print("Pls type '1' or '2'. The Programm will stop now.")
    sys.exit()


    
