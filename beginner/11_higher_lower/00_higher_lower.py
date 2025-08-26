from art import logo
from art import vs
from game_data import data
import random

def print_logo():
    print("\n" * 20)
    print(logo, end="")

def evaluate_choice(selected, game_score, playerA, playerB):
    if selected == "A":
        if playerA["follower_count"] > playerB["follower_count"]:
            print_logo()
            game_score += 1
            print(f"You're right! Current Score: {game_score}")
            return game_score    
        else:
            print_logo()
            print(f"Sorry, that's wrong. Final score: {game_score}")
            return game_score
    elif selected == "B":
        if playerB["follower_count"] > playerA["follower_count"]:
            game_score += 1
            print_logo()
            print(f"You're right! Current Score: {game_score}")
            return game_score
        else:
            print_logo()
            print(f"Sorry, that's wrong. Final score: {game_score}")
            return game_score
    else:
        print_logo()
        print(f"Sorry, that's wrong. Final score: {game_score}")
        return game_score
        
def start_game():
    print_logo()
    score = 0
    game_runs = True

    while game_runs == True:
        pA = random.choice(data)
        pB = random.choice(data)
        print(f"Compare A: {pA["name"]}, a {pA["description"]}, from {pA["country"]}")
        print(vs, end="")
        print(f"Against B: {pB["name"]}, a {pB["description"]}, from {pB["country"]}")
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        score_check = score
        score = evaluate_choice(choice, score, pA, pB)
        if score == score_check:
            game_runs = False

start_game()