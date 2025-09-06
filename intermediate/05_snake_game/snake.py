from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake = []
        x = 0
        for _ in range(3):
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.goto(x, 0)
            self.snake.append(segment)
            x -= 20

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)
        self.snake[0].forward(20)