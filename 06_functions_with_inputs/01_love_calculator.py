#! usr/bin/env python3

def calculate_love_score(name1, name2):
    name1 = name1.upper()
    name2 = name2.upper()
    score_1 = 0
    score_2 = 0
    for letter in "TRUE":
        for letter2 in name1:
            if letter2 == letter:
                score_1 += 1
        for letter2 in name2:
            if letter2 == letter:
                score_1 += 1
    for letter3 in "LOVE":
        for letter4 in name2:
            if letter4 == letter3:
                score_2 += 1
        for letter4 in name1:
            if letter4 == letter3:
                score_2 += 1
    final_score = str(score_1) + str(score_2)
    print(final_score)
    
calculate_love_score("Divine", "Intervention")
