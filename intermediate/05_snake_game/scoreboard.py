from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("data.txt") as high_score_file:
            self.high_score = int(high_score_file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score = {self.current_score} | High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.write(f"Score = {self.current_score} | High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        with open("data.txt", mode="w") as high_score_file:
            high_score_file.write(str(self.high_score))
        self.current_score = 0
        self.update()

    def increase_score(self):
        self.current_score += 1
        self.update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
