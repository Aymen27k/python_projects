# import colorgram
from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.colormode(255)

#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color_obj in colors:
#     rgb = color_obj.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_colors.append(rgb_tuple)
#
# print(rgb_colors)

color_list = [(136, 169, 200), (191, 162, 140),
              (64, 89, 135), (183, 153, 171), (119, 77, 99), (153, 75, 50), (55, 118, 94), (220, 228, 87),
              (113, 115, 181),
              (45, 52, 105), (37, 44, 59), (129, 194, 143), (177, 187, 212), (225, 134, 16), (176, 94, 112),
              (81, 49, 66),
              (58, 46, 57), (110, 39, 37), (108, 166, 73), (215, 179, 193), (40, 49, 45), (46, 38, 35), (221, 83, 45),
              (231, 176, 158), (23, 95, 80), (148, 206, 214)]
width_pos = (-screen.window_width() / 2)
height_pos = (-screen.window_height() / 2)
t.shape("arrow")
t.penup()
t.hideturtle()
t.goto(width_pos, height_pos)


def draw_dots():
    for dot in range(10):
        t.pendown()
        t.dot(20, random.choice(color_list))
        t.penup()
        t.forward(50)


if __name__ == "__main__":
    for line in range(10):
        draw_dots()
        height_pos += 50
        t.goto(width_pos, height_pos)




screen.exitonclick()
