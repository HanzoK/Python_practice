# FileNotFound

# try:
#     file = open("wow.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("wow.txt", mode="w")
#     file.write("Why hello there!")
# except KeyError as error_msg:
#     print(f"Whoops, {error_msg} doesn't exist!")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error I made up")

# KeyError
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]

# def count_likes(posts):
#     total_likes = 0
#     for post in posts:
#         try:
#             total_likes = total_likes + post['Likes']
#         except:
#             print("There is an entry without any likes.")
#     return total_likes

# count_likes(facebook_posts)

# IndexError
# fruits = ["Apple", "Pear", "Orange"]
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except:
#         fruit = "Fruit"
#     finally:
#         print(fruit + " pie")

# make_pie(4)

# TypeError
# text = "wow"
# print(text + 5)

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("That's a ridiculous height for a human!")

bmi = weight/ height**2
print(bmi)