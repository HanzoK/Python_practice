#! usr/bin/env python 3

programming_dictionary = {
        "Bug": "An error in a program that prevents the program from running as expected.",
        "Loop": "The action of doing something over and over again.",
}

print(programming_dictionary["Bug"])

# Adding an item to the dictionary
programming_dictionary["Function"] = "A piece of code that you can easily call over and over again."

print(programming_dictionary["Function"])
print("\n")
print(programming_dictionary)

# Wipe an existing dictionary
print("\n")
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
print("\n")
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
print("\n")
for key in programming_dictionary
    print(key)
    print(programming_dictionary[key])
