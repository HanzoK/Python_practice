from data import MENU, RESOURCES
from art import logo

def report():
    print(f"Water: {RESOURCES["water"]}ml")
    print(f"Milk: {RESOURCES["milk"]}ml")
    print(f"Coffee: {RESOURCES["coffee"]}g")
    print(f"Money: ${RESOURCES["money"]}")

def sufficient_cash(total_cash, drink):
    if total_cash < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return True
        
def update_resources(cash_obtained, drink):
    for item in MENU[drink]["ingredients"]:
        amount = MENU[drink]["ingredients"][item]
        if RESOURCES[item] < amount:
            print(f"Sorry there is not enough {item}.")
            return False
        elif item in RESOURCES:
            RESOURCES[item] -= amount
    RESOURCES["money"] += cash_obtained
    return True

def process_order(chosen_drink):
    print("Please insert coins.")
    sum_cash = int(input("How many quarters?: ")) * 0.25
    sum_cash += int(input("How many dimes?: ")) * 0.1
    sum_cash += int(input("How many nickles?: ")) * 0.05
    sum_cash += int(input("How many pennies?: ")) * 0.01
    enough_money = sufficient_cash(sum_cash, chosen_drink)
    if enough_money == True:
        cash_return = sum_cash - MENU[chosen_drink]["cost"]
        profit = sum_cash - cash_return
        enough_resources = update_resources(profit, chosen_drink)
    if enough_money == False or enough_resources == False:
        return
    if sum_cash > MENU[chosen_drink]["cost"]:
        print(f"here is ${cash_return} in change.")
        print(f"Here is your {chosen_drink}. Enjoy!")
        return 

print(logo)
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        report()
    elif choice == "off":
        is_on = False
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        process_order(choice)
    else:
        print("Beep Boop. Unknown command. Please try again.")