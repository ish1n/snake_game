from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("green")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))
        self.ht()

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))

    def collison_wall(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
