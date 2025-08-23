#! usr/bin/env python 3

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissor]
ai_choice = choices[random.randint(0, 2)]

input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")

if input == "0":
    print(rock)
elif input == "1":
    print(paper)
elif input == "2":
    print(scissor)
else:
    print("Bruh.")
    exit()

print(f"Computer chose: {ai_choice}")

if ai_choice == choices[int(input)]:
    print("Wow. A draw. How nice.")
elif input == "0":
    if ai_choice == paper:
        print("Heh. Loser.")
    else:
        print("Fine. You win this time...")
elif input == "1":
    if ai_choice == scissor:
        print("Heh. Loser.")
    else:
        print("Fine. You win this time...")
elif input == "2":
    if ai_choice == rock:
        print("Heh. Loser.")
    else:
        print("Fine. You win this time...")
