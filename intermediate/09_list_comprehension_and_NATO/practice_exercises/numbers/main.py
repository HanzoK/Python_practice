numbers = [1, 2, 3]
new_numbers = [item + 1 for item in numbers]
print(new_numbers)

name = "Han"
new_list = [letter for letter in name]
print(new_list)

nums = [_ * 2 for _ in range(1, 5)]
print(nums)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

capital_names = [name.upper() for name in names if len(name) > 4]
print(capital_names)