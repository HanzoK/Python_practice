from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color(red/orange/yellow/green/blue/purple): ").lower()
turtles = []
race_over = False

def prepare_turtles():
    y = -75
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(-230, y)
        turtles.append(new_turtle)
        y += 30

def start_race():
    race_over = False
    while race_over == False:
        for turtle in turtles:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"Congratulations! You bet on the right turtle, {winning_color}!")
                    race_over = True
                else:
                    print(f"Sorry, but {winning_color} was the faster turtle. Better luck next time!")
                    race_over = True
                break
            turtle.forward(random.randint(1, 10))


if user_bet in colors:
    prepare_turtles()
    start_race()
else:
    user_bet = screen.textinput(title="Make your bet", prompt="What sort of color is that? Try again. Enter a color(red/orange/yellow/green/blue/purple): ").lower()
screen.exitonclick()