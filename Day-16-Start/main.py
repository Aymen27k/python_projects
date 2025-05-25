# import turtle
#
# aymen = turtle.Turtle()
#
# aymen.shape("turtle")
# for x in range(0, 9):
#     aymen.forward(20)
#     aymen.color("red")
#     for i in range(0, 9):
#         aymen.left(5)
#         aymen.forward(20)
#         aymen.color("blue")
#
#     #     aymen.forward(50)
#     #     aymen.right(90)
#     #     aymen.forward(50)
#     #     aymen.right(90)
#     #     aymen.forward(50)
#     #     aymen.right(90)
#     #     aymen.forward(50)
#     # aymen.forward(100)
#     # aymen.color("Blue")
#
# my_screen = turtle.Screen()
# my_screen.exitonclick()
# print(my_screen.canvheight)
# print(aymen)

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtel", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
table.header = True
print(table)
