from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 28, "normal")


class Scores(Turtle):
    def __init__(self, l_player, r_player):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.l_score = 0
        self.r_score = 0
        self.l_player = l_player
        self.r_player = r_player

    def draw_the_net(self):
        self.goto(0, 300)
        self.setheading(270)
        for y in range(600):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

    def score_display(self):
        self.draw_the_net()
        self.goto(-225, 250)
        self.write(f"{self.l_player} : {self.l_score}", False, ALIGNMENT, FONT)
        self.goto(225, 250)
        self.write(f"{self.r_player} : {self.r_score}", False, ALIGNMENT, FONT)

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.score_display()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.score_display()

    def winner(self, player):
        self.clear()
        self.goto(0, 0)
        self.write(f"{player} Won", False, ALIGNMENT, FONT)
