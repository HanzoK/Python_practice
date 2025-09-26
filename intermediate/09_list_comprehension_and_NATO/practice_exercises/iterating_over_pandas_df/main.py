student_dict = {
    "student": ["Han", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)

import pandas as pd

student_df = pd.DataFrame(student_dict)
print(student_df)

# Loop through df

for (index, row) in student_df.iterrows():
    # print(index)
    # print(row)
    print(row.student)
    print(row.score)