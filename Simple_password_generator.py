#!/usr/bin/python3

import sys
import random
import getpass
import time
start = time.time()

password_options = ["1234567890", "abcdefghijklmopqrstxyz", "!@#$%", "abcdefghijklmopqrstxyz".upper()]

print("CLI PASSWORD GENERATOR")
print("*" * 80)
print()

try:
    password_length = int(input("Choose password length: "))
    characters_list = []
    for i in range(0, password_length):
        characters_list.append(random.choice("".join(password_options)))
    print("Generated password: {}".format("".join(characters_list)))
except KeyboardInterrupt:
    print()
    print("Program interrupted by the user: {}".format(getpass.getuser()))
    print("Terminating program...")
    sys.exit()
except ValueError:
    print()
    print("Password length has to be a number")
    sys.exit()

end = time.time()
print("Execution time: {} seconds".format(round(float(end - start),2)))

