with open("file1.txt") as file1_data:
    file1_nums = file1_data.read().splitlines()

with open("file2.txt") as file2_data:
    file2_nums = file2_data.read().splitlines()

result = [int(num) for num in file1_nums if num in file2_nums]

print(result)