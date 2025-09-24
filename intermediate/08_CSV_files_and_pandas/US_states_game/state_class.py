from turtle import Turtle

class state(Turtle):
    
    def __init__(self, state_name, x, y):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(x, y)
        self.write(state_name, align="center", font=("Arial", 10, "bold"))

