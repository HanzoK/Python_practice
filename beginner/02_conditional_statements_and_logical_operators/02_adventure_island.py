#! usr/env/bin python 3

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")

direction = input("Type \"left\" or \"right\"\n").lower()
if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    action = input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n"),lower()
    if action == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door = input("One red, one yellow and one blue. Which colour do you choose? \"red\", \"yellow\" or \"blue\"?\n").lower()
        if door == "yellow":
            print("Congratulations!!! You have found the treasure!!! Time to spend that money on blackjack and fair ladies!")
        elif door == "red":
            print("Too lazy right now. I'll think of an appropriate death for you later on.")
        elif door == "blue":
            print("Wow. Wrong door. You get squashed to death but a magical 1000 ton anvil falling on top of your head. So close yet so far.... Oh well! You are dead.")
        else:
           print("Alright, that's it. I'm sick of your constant testing for different options. I'll send you right back to the beginning of this game. TAKE THAT!")
    elif action == "swim":
        print("What were you thinking? Trying to cross such a huge lake by swimming across? Oh well, have fun sleeping with the fishes tonight! You are dead.")
    else:
        print("...Seriously? What kind of action is that? Are you alright? Whatever. Restart the game!")
elif direction == "right":
    print("Congratulations. Bandits ambush you, dropkick you and leave you behind with no valuables left. You are dead.")
else:
    print("What kind of direction is that? Can you tell left from right? Next!")
