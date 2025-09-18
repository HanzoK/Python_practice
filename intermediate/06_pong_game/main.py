from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Player((350, 0))
paddle_l = Player((-350, 0))
ball = Ball()
scorebaord = Scoreboard()

screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.distance(paddle_r) < 50 and ball.xcor() > 335 or ball.distance(paddle_l) < 50 and ball.xcor() < -335:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_pos()
        scorebaord.l_point()
    if ball.xcor() < -390:
        ball.reset_pos()
        scorebaord.r_point()

screen.exitonclick()
