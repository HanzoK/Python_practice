#! usr/bin/env python 3

from cipher_art import logo
from alphabet import alphabet

# def encrypt(original_text, shift_amount):
#     encrypted_text = ""
#     for letter in original_text:
#         encrypted_text += alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)]
#     return encrypted_text
#
# def decrypt(original_text, shift_amount):
#     encrypted_text = ""
#     for letter in original_text:
#         encrypted_text += alphabet[(alphabet.index(letter) - shift_amount) % len(alphabet)]
#     return encrypted_text

def caesar(original_text, shift_amount, action):
    encrypted_text = ""
    if action == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            encrypted_text += letter
            continue
        encrypted_text += alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)]
    print(f"Here is the {action}d result: {encrypted_text}\n")

print(logo)
flag = 1

while(flag == 1):
    action = input("Type \'encode\' to encrypt, type \'decode\' to decrypt:\n").lower()

    if action == "encode":
        message = input("Type your message:\n").lower()
        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("What are you doing? That's not a number?!")
            continue
        encoded = caesar(message, shift, action)

    elif action == "decode":
        message = input("Type your message:\n").lower()
        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("What are you doing? That's not a number?!")
            continue
        encoded = caesar(message, shift, action) 

    else:
        print("I mean, seriously? You had one job.")

    go_again = input("Type \'yes\' if you want to go again. Otherwise, type \'no\'.\n").lower()
    if go_again == "no":
        flag = 0
        print("Well, I guess that's it, huh? Until next time then.")
    else:
        print("...surely you know how to answer a \'yes\' or \'no\' question, right? RIGHT? Let's do this again!")
