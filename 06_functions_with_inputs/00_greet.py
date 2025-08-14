#! usr/bin/env python 3

# def greet():
#     print("Hello ", end = "")
#     print("World", end = "")
#     print("!", end = "")
#
# greet()

# *******Functions that allows for inputs*******

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do, {name}?")
#
# greet_with_name("Han")

# *******Functions that allow for multiple inputs*******

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet_with("Han", "Vienna")
greet_with("Vienna", "Han")
greet_with(location = "Vienna", name = "Han")
