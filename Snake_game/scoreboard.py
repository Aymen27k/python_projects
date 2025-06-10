from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Consolas", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.screen= Screen()
        self.hideturtle()
        self.penup()
        self.getting_high_score()
        self.high_score_name
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score_name}=> {self.high_score}", False, ALIGNMENT,
                   FONT)

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"Game over! Final score is: {self.score}", False, ALIGNMENT, FONT)
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_name = self.screen.textinput("A new High Score", 'Enter your name: ')
        self.saving_high_score()
        self.score = 0
        self.update_score()

    def game_paused(self):
        self.goto(0, 0)
        self.write(f"Game Paused !", False, ALIGNMENT, FONT)

    def getting_high_score(self):
        with open("data.txt", 'r') as file:
            data = file.read()
        parts = data.split(',')
        self.high_score_name = parts[0]
        self.high_score = int(parts[1])

    def saving_high_score(self):
        with open("data.txt", 'w') as file:
            formatted_data = f"{self.high_score_name},{self.high_score}"
            file.write(str(formatted_data))
