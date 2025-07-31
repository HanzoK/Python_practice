#! usr/bin/env python 3

i = 0
for number in range(1, 101):
    s = ""
    if(number % 3 == 0):
        s += "Fizz"
    if(number % 5 == 0):
        s += "Buzz"
    if(number % 7 == 0):
        s += "Zazz"
    if (s == ""):
        s = number
    print(s)
