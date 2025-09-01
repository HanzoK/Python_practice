import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour_tuple = (r, g, b)
    return colour_tuple

# def forward_and_right():
#     """draw a square"""
#     tim.right(90)
#     tim.forward(100)

# def draw_fashed_line():
#     """draw a dashed line"""
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# def draw_shapes(sides):
#     """draws different shapes based on number of sides"""
#     for _ in range(sides):
#         tim.right(360/sides)
#         tim.forward(100)

# def random_walk():
#     """walk around aimlessly on the screen"""
#     tim.width(10)
#     tim.pen(speed=10)
#     directions = [0, 90, 180, 270]
#     tim.setheading(random.choice(directions))
#     tim.color(random_colour())
#     tim.forward(20)

def spirograph(size_of_gap):
    tim.speed("fastest")
    circles_drawn = 360/size_of_gap
    for _ in range(int(circles_drawn)):
        tim.color(random_colour())
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)

spirograph(5)

screen = t.Screen()
screen.exitonclick()