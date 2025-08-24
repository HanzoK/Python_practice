from calculator_art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    print("hello")
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

result = 0
continue_or_not = ""

while(True):
    if continue_or_not != "y":
        num1 = float(input("What's the first number?: "))
    else:
        num1 = result
    for symbol in operations:
        print(symbol)
    operation = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    result = operations[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {result}")
    continue_or_not = input("Type \'y\' to continue calculating with {result}, ot type \'n\' to start a new calculation: ").lower()
    