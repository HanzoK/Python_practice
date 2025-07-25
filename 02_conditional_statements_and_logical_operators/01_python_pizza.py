#! /usr/bin/env python 3

print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want! S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25

if pepperoni == "Y":
    if size == "M" or size == "L":
        price += 3
    else:
        price += 2

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}")
