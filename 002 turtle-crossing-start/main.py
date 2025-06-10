import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.listen()

player = Player()
# Creating Cars
car_manager = CarManager()
scoreboard = Scoreboard()
screen.title("Turtle Cross Game | Made by Aymen")
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:

    car_manager.create_car()
    car_manager.move_cars()
    screen.onkey(player.move_up, "Up")
    # Detect collision with Cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    # Detect successful crossing
    if player.arrived():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
