from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Consolas", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game over! Final score is: {self.score}", False, ALIGNMENT, FONT)

    def game_paused(self):
        self.goto(0, 0)
        self.write(f"Game Paused !", False, ALIGNMENT, FONT)
