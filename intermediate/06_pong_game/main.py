from turtle import Screen
from player import Player

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")


paddle_1 = Player()
paddle_2 = Player()
paddle_1.goto(350, 0)
paddle_2.goto(-350, 0)
paddle_1.showturtle()
paddle_2.showturtle()

screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")

screen.exitonclick()
