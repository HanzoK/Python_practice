# FileNotFound

try:
    file = open("wow.txt")
    a_dict = {"key":"value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("wow.txt", mode="w")
    file.write("Why hello there!")
except KeyError as error_msg:
    print(f"Whoops, {error_msg} doesn't exist!")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File is finally closed")
    
# KeyError
# a_dict = {"key": "value"}
# value = a_dict{"what_key_is_this?"}

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[69]

# TypeError
# text = "wow"
# print(text + 5)

# try:

# except:

# else:

# finally: