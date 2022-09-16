from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Ariel", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.highscore = 0
        with open("text.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.goto(0, 270)
        self.score = 0
        self.color("white")
        self.score_track()

    def reset_scoreboard(self):
        if self.highscore < self.score:
            self.highscore = self.score-1

        # contents = 0

        with open("text.txt", mode="r") as file:
            contents = int(file.read())

        if contents < self.highscore:
            with open("text.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.score_track()

    def score_track(self):
        self.clear()
        self.write(f"Score : {self.score} | High Score : {self.highscore}", False, align=ALIGNMENT, font=FONT)
        self.score += 1
        return self.score

    # def game_over(self):
    #     self.reset_scoreboard()
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
