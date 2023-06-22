from turtle import Turtle

ALIGNMENT = "center"

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 220)
        self.color("white")
        self.score_writter()
        self.hideturtle()

    def score_writter(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def refresh_score(self, bonus):
        self.score += bonus
        self.clear()
        self.score_writter()

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"Game Over your score: {self.score}", align=ALIGNMENT, font=FONT)
