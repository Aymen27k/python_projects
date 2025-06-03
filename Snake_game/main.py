from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def main():
    # Screen setup
    screen = Screen()
    screen.tracer(0)
    screen.setup(width=600, height=600)

    screen.title("Snake Game! Made by Aymen")
    screen.bgcolor("black")
    # Creating Snake
    snake = Snake()
    food = Food()
    score = Scoreboard()

    # Screen listener
    screen.listen()
    screen.onkey(snake.go_up, "Up")
    screen.onkey(snake.go_down, "Down")
    screen.onkey(snake.go_left, "Left")
    screen.onkey(snake.go_right, "Right")
    screen.onkey(snake.toggle_pause, "p")
    screen.onkey(snake.toggle_pause, "P")
    # Moving The Snake
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        if snake.is_paused:
            pass
        else:
            snake.moving_snake()

            # Detecting collision with food
            if snake.head.distance(food) < 15:
                food.refresh()
                score.increase_score()
                snake.add_segment()
            # Detect Wall detection
            if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
                game_is_on = False
                score.game_over()

            # Detect Tail collision
            for segment in snake.segments[1:]:
                if snake.head.distance(segment) < 10:
                    game_is_on = False
                    score.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    main()
