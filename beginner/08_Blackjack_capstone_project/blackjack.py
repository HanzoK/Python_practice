from blackjack_art import logo
import random

'''Project made with 4 rules in mind
1. The deck has unlimited size
2. There are no jokers
3. The Jack/Queen/King all count as 10
4. The Ace can count as 11 or 1
'''
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def your_cards_and_score(your_cards):
    cardsum = 0
    for item in your_cards:
        cardsum += item
        if your_cards[-1] == 11 and cardsum < 21:
            your_cards[-1] = 1
    print(f"    Your cards: {your_cards}, current score: {cardsum}")
    return cardsum

def final_scores(your_cards, cpu_cards, your_score, cpu_score):
    print(f"    Your final hand: {your_cards}, final score: {your_score}")
    print(f"    Computer's final hand: {cpu_cards}, final score: {cpu_score}")
    if your_score > 21:
        print("You went over. You lose :(")
    elif cpu_score > 21:
        print("Opponent went over. You win :D")
    elif your_score > cpu_score:
        print("Yay! You won!")
    elif your_score == cpu_score:
        print("Draw :/")
    else:
        print("You lose :(")

def draw_cards(your_cards, cpu_cards, your_score):
    your_score = your_cards_and_score(your_cards)
    print(f"    Computer's first card: {cpu_cards[0]}")
    while your_score < 22:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
            your_cards.append(random.choice(cards))
            if your_cards[-1] == 11 and your_score > 21:
                your_cards[-1] = 1
            your_score = your_cards_and_score(your_cards)
            print(f"    Computer's first card: {cpu_cards[0]}")
        elif another_card == "n":
            break
    return your_score

def cpu_draw_cards(cpu_cards, cpu_score, player_score):
    while cpu_score < 21 and cpu_score < player_score:
        cpu_cards.append(random.choice(cards))
        cpu_score += cpu_cards[-1]
    return cpu_score

def game_loop():

    your_score = 0
    cpu_score = 0
    your_cards = []
    cpu_cards = []
    your_cards.append(random.choice(cards))
    your_cards.append(random.choice(cards))
    cpu_cards.append(random.choice(cards))
    cpu_score = cpu_cards[0]
    your_score = draw_cards(your_cards, cpu_cards, your_score)
    if your_score > 21:
        final_scores(your_cards, cpu_cards, your_score, cpu_score)
        return
    cpu_score = cpu_draw_cards(cpu_cards, cpu_score, your_score)
    final_scores(your_cards, cpu_cards, your_score, cpu_score)

def start_game():
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start == "y":
        print(f"{logo}\n")
        game_loop()
        start_game()
    else:
        print("You're no fun.")

start_game()