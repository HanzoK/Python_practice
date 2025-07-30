#! usr/bin/env python 3

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]

j = 0
for i in student_scores:
    if i > j:
        j = i

print(j)
