#!/usr/bin/env python 3

# height = 1.65 
# weight = 84

weight = input("What's your weight?\n")
height = input("What's your height?\n")
# Write your code here.
# Calculate the bmi using weight and height.

bmi = float(weight) / float(height)**2

print((bmi)*10000)
