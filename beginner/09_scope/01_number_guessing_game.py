import random
from guessing_art import logo

def check_guess(guessed_num, target, found_flag):
    if guessed_num > 100 or guessed_num < 1:
        print("Really? I said a number between 1 and 100. I'll take off an attempt for that anyways.")
    elif guessed_num > target:
        print("Too high.")
    elif guessed_num < target:
        print("Too low.")
    else:
        found_flag = True
        print(f"You got it! The answer was {target}.")
        return found_flag
    print("Guess again.")
    return found_flag 

def game_loop(attempts):
    targetnr = random.randint(1, 100)
    nr_found = False
    while attempts > 0 and nr_found == False:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts -= 1
        if attempts == 0:
            return print("You've run out of guesses, you lose.")
        nr_found = check_guess(guess, targetnr, nr_found)

def start_game():
    tries = 0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        tries = 10
        game_loop(tries)
    elif difficulty == "hard":
        tries = 5
        game_loop(tries)
    else:
        print("Never heard of this mode.")
        start_game()

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
start_game()