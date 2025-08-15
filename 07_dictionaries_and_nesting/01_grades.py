#! /usr/bin/env python3

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for item in student_scores:
    if student_scores[item] > 90 and student_scores[item] <= 100:
        student_grades[item] = "Outstanding"
    elif student_scores[item] > 80:
        student_grades[item] = "Exceeds Expectations"
    elif student_scores[item] > 70:
        student_grades[item] = "Acceptable"
    else:
        student_grades[item] = "Fail"

print(student_grades)
