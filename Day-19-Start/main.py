from turtle import Turtle, Screen

aymen = Turtle()


def move_forward():
    aymen.forward(50)


def move_backward():
    aymen.backward(50)


def turn_left():
    aymen.left(10)


def turn_right():
    aymen.right(10)


def draw_left_curve():
    aymen.forward(50)
    aymen.left(30)


def draw_right_curve():
    aymen.forward(50)
    aymen.left(30)


def clear_screen():
    aymen.clear()
    aymen.teleport(0, 0)
    aymen.setheading(0)


screen = Screen()
screen.listen()

# Key listeners
screen.onkey(move_forward, "z")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "q")
screen.onkey(turn_right, "d")
screen.onkey(draw_left_curve, "a")
screen.onkey(draw_right_curve, "e")
screen.onkey(clear_screen, "c")
screen.onkey(exit, "Escape")

screen.exitonclick()
