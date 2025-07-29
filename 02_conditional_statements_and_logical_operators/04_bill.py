#! usr/bin/env python3

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
length = len(friends)
num = random.randint(0, length - 1)
result = friends[num]
print(result)
