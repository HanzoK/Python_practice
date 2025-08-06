#! usr/bin/env python 3

import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
stages = hangman_art.stages
lives = 6
game_over = False
correct_letters = []

while not game_over:
    print(f"******************** {lives} / 6 LIVES LEFT*********************\n")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print(stages[lives])
        print("1 letter, do I have to repeat myself?")
        continue
    elif guess in correct_letters:
        print(stages[lives])
        print("You already guessed that letter.")
        continue

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display + "\n")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print(f"HAH! Loser. The word was '{chosen_word}'.")
            game_over = True

    if "_" not in display:
        game_over = True
        print("Congrats. You win!")

    print(stages[lives])
