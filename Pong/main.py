from turtle import Screen
from scoreboard import Scores
from paddle import Paddle
from ball import Ball
import time


def main():
    # Main screen initialization
    screen = Screen()

    screen.tracer(0)
    screen.setup(width=900, height=600)
    screen.bgcolor("black")
    screen.title("Pong | Made by Aymen")
    # Players name inputs
    first_player = screen.textinput(title="Player 1",
                                     prompt="Enter left player name : ")
    second_player = screen.textinput(title="Player 2",
                                     prompt="Enter right player name : ")
    l_player_name = first_player.capitalize()
    r_player_name = second_player.capitalize()
    score = Scores(l_player_name, r_player_name)
    score.draw_the_net()
    score.score_display()
    ball = Ball()

    left_paddle = Paddle(-420)
    right_paddle = Paddle(420)
    screen.listen()
    game_is_on = True
    while game_is_on:

        ball.ball_motion()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < - 270:
            ball.bounce_y()

        # Detect collision with the paddles
        if ball.distance(right_paddle) < 20 and ball.xcor() > 395 or ball.distance(
                left_paddle) < 20 and ball.xcor() < - 395:
            ball.bounce_x()

        # Detect ball goes beyond the right limits
        if ball.xcor() > 460:
            score.l_point()
            ball.reset_ball()

        # Detect ball goes beyond the left limits
        if ball.xcor() < -460:
            score.r_point()
            ball.reset_ball()
        # Win condition
        if score.l_score == 7:
            score.winner(l_player_name)
            ball.hideturtle()
            game_is_on = False
        elif score.r_score == 7:
            score.winner(r_player_name)
            ball.hideturtle()
            game_is_on = False
        # Movement trigger
        # Left Paddle
        screen.onkey(left_paddle.move_up, "z")
        screen.onkey(left_paddle.move_down, "s")
        # Right Paddle
        screen.onkey(right_paddle.move_up, "Up")
        screen.onkey(right_paddle.move_down, "Down")

        screen.update()
        time.sleep(ball.move_speed)
    screen.exitonclick()


if __name__ == "__main__":
    main()
