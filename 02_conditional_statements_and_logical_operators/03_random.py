#! usr/bin/env python 3

import random

# random_int = random.randint(1, 10)
# print(random_int)

# random_num = random.random()
# print(random_num)

# random_float = random.uniform(1, 10)
# print(random_float)

result = random.randint(0, 1)
if result == 0:
    print("Tails")
elif result == 1:
    print("Heads")
