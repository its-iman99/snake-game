from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Ariel", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.color("white")
        self.score_track()

    def score_track(self):
        self.clear()
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)
        self.score += 1
        return self.score

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
