# import colorgram as cg

# colors = cg.extract("image.jpg", 50)

# extracted_colours = []

# def rgb_to_tuple(color_class):
#     r = color_class.r
#     g = color_class.g
#     b = color_class.b
#     color_tuple = (r, g, b)
#     return color_tuple

# for item in colors:
#     created_tuple = rgb_to_tuple(item.rgb)
#     extracted_colours.append(created_tuple)

# print(extracted_colours)

import turtle as t
import random

t.colormode(255)

screen = t.Screen()
tim = t.Turtle()
tim.speed("fastest")
tim.shape("arrow")
tim.pensize(50)
tim.penup()
tim.hideturtle()

colour_list = [(250, 228, 16), (212, 13, 9), (199, 12, 36), (230, 228, 6), (196, 70, 20), (32, 90, 188), (235, 148, 38), (43, 212, 70), (33, 30, 152), (16, 22, 54), (67, 9, 48), (244, 39, 150), (14, 206, 223), (66, 202, 229), (62, 21, 10), (225, 19, 111), (15, 155, 21), (228, 166, 9), (248, 11, 9), (245, 58, 16), (98, 75, 9), (223, 140, 203), (68, 240, 160), (10, 97, 62), (6, 39, 33), (68, 219, 157), (238, 157, 211), (91, 77, 205), (88, 225, 234), (250, 8, 12), (242, 166, 157), (178, 181, 224), (35, 242, 166), (9, 80, 112), (11, 59, 246)]

x = -250
y = -150
dots = 10
rows = 10

def draw_row():
    for _ in range(dots):
        tim.color(random.choice(colour_list))
        tim.dot(20)
        tim.forward(50)

def go_to_next_row(current_position):
    tim.goto(current_position)
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    return (tim.position())

def start_painting():
    tim.goto(x, y)
    current_pos = tim.position()
    for _ in range(rows):
        draw_row()
        tim.goto(current_pos)
        current_pos = go_to_next_row(tim.position())

start_painting()

screen.exitonclick()
