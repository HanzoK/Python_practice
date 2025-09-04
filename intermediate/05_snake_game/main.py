from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("HanzoK's Snake Game")
screen.tracer(0)

game_is_running = True
segments = []
x = 0
for _ in range(3):
    snake = Turtle(shape="square")
    snake.penup()
    snake.color("white")
    snake.goto(x, 0)
    segments.append(snake)
    x -= 20

while game_is_running:
    screen.update()
    time.sleep(0.1)
    for segment in range(len(segments) - 1, 0, -1):
        if segments[0].xcor() > 270:
            game_is_running = False
        new_x = segments[segment - 1].xcor()
        new_y = segments[segment - 1].ycor()
        segments[segment].goto(new_x, new_y)
    segments[0].forward(20)












screen.exitonclick()