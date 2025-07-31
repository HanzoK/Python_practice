#! usr/bin/env python 3

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

input = input("Guess a letter:\n").lower()

if len(input) != 1:
    print("1 letter, do I have to repeat myself?")
    exit()

for i in range(0, len(chosen_word)):
    if input == chosen_word[i]:
        print("Right.")
    else:
        print("Wrong.")
