#! usr/bin/env python 3

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""

print("Welcome to the PyPassword Generator!")
nletters = int(input("How many letters would you like in your password?\n"))
nsymbols = int(input("How many symbols would you like?\n"))
nnumbers = int(input("How many numbers would you like?\n"))

npassword = nletters + nsymbols + nnumbers
if npassword < 8:
    print("Too few characters. Need at least 8 characters!")
    exit()

for i in range(0, nletters):
    password += random.choice(letters)

for j in range(0, nsymbols):
    password += random.choice(symbols)

for k in range(0, nnumbers):
    password += random.choice(numbers)

print (f"Here is your password: {password}")


password_array = []
for l in password:
    password_array += [l]

random.shuffle(password_array)
new_password = ""

for y in range(0, len(password_array)):
    new_password += password_array[y]

print(f"Here is your new randomly generated password: {new_password}")
