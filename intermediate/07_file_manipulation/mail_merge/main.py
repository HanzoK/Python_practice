with open("./Input/Names/invited_names.txt") as file:
    data = file.read().splitlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    read_letter = letter.read()

for name in data:
    stripped_name = name.strip() 
    named_letter = read_letter.replace("[name]", stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as new_letter:
        new_letter.write(named_letter)