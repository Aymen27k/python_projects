from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(starting_position, 0)
        self.shapesize(5, 1)

    def move_up(self):
        if self.ycor() < 230:
            self.setposition(x=self.xcor(), y=self.ycor() + 20)

    def move_down(self):
        if self.ycor() > - 230:
            self.setposition(x=self.xcor(), y=self.ycor() - 20)
