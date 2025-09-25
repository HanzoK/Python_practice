sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
split_str = sentence.split()
result = {word:len(word) for word in split_str}
print(result)