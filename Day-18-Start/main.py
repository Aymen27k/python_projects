from turtle import Turtle, Screen
import random

DIRECTIONS = [0, 90, 180, 270]

screen = Screen()

screen.colormode(255)


def create_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


aymen = Turtle()
aymen.shape("turtle")
aymen.color(create_color())


#
# for i in range(4):
#     aymen.forward(100)
#     aymen.left(90)

# for i in range(15):
#     aymen.forward(10)
#     aymen.pu()
#     aymen.forward(10)
#     aymen.pd()
def draw_shape(num_sides):
    aymen.color(create_color())
    angle = 360 / num_sides
    for _ in range(num_sides):
        aymen.forward(100)
        aymen.left(angle)


def random_walk():
    aymen.width(10)
    for i in range(200):
        aymen.speed(random.randint(0, 15))
        aymen.color(create_color())
        aymen.forward(50)
        aymen.setheading(random.choice(DIRECTIONS))


def spirograph(size_of_gap):
    aymen.speed(25)
    for _ in range(int(360 / size_of_gap)):
        aymen.color(create_color())
        aymen.circle(100)
        aymen.setheading(aymen.heading() + size_of_gap)


# for num_sides_n in range(3, 11):
#     draw_shape(num_sides_n)
spirograph(5)
# random_walk()

screen.exitonclick()
