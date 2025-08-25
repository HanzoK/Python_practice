from blackjack_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def game_start():
    print(logo)
    print("\n")


start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if start == "y":
    game_start()
elif start == "n":
    print("You're no fun.")