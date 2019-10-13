#!/usr/bin/python3

import time
import sys
import random

password_options = ["1234567890", "abcdefghijklmopqrstxyz", "!@#$%", "abcdefghijklmopqrstxyz".upper()]

print("CLI PASSWORD GENERATOR")
print("*" * 80)
user_choice = input('Would you like to generate password? y/n ')
print()
if (user_choice in ("yes", "y")):
    password_length = int(input("Choose password length: "))
    characters_list = []
    for i in range(0, password_length):
        characters_list.append(random.choice("".join(password_options)))
    print("Generated password: {}".format("".join(characters_list)))
else:
    print("Exiting program...")
    sys.exit()
