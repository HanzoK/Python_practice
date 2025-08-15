#! usr/bin/env python 3

from gavel_art import logo

print(logo)
print("Welcome to the secret auction program.")

flag = True
max = 0
winner = ""
auction = {}

while (flag == True):
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    more_players = input("Are there any other bidders? Type \'yes\' or \'no\'.\n").lower()
    print("\n" * 100) 
    auction[name] = bid
    if more_players == "no":
        flag = False

for person in auction:
    if auction[person] > max:
        max = auction[person]
        winner = person

print(f"The winner is {person} with a bid of ${max}.")
