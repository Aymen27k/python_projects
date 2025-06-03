from turtle import Turtle, Screen
import random
import time


def main():
    continue_playing = False
    while not continue_playing:
        is_race_on = False
        screen = Screen()

        screen.title("Turtle Race!")
        screen.setup(width=1000, height=800)
        all_turtles = []
        aymen = Turtle("turtle")
        aymen.hideturtle()
        aymen.penup()
        aymen.goto(0, 350)
        x = -480
        y = -100
        user_bet = screen.textinput(title="Make your bet",
                                    prompt="Which Turtle will win the race? Enter a color : ").lower()
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        for turtle_index in range(6):
            new_turtle = Turtle("turtle")
            new_turtle.color(colors[turtle_index])
            new_turtle.penup()
            all_turtles.append(new_turtle)
            new_turtle.goto(x, y)
            y += 50
        if user_bet:
            is_race_on = True
        aymen.write("Race is underway !", move=False, align="center", font=("Arial", 24, "normal"))
        aymen.goto(0, 290)
        current_leader = -450
        while is_race_on:

            for turtle in all_turtles:
                if turtle.xcor() > 480:
                    is_race_on = False
                    winning_color = turtle.pencolor()
                    if user_bet == winning_color:
                        print(f"You've Won ! The {winning_color} Turtle is the winner !")
                    else:
                        print(f"You lost the bet ! {winning_color} Turtle is the winner !")
                rand_distance = random.randint(0, 30)
                turtle.forward(rand_distance)
                if turtle.xcor() > current_leader:
                    turtle_leader = turtle.pencolor()
                    current_leader = turtle.xcor()
                    aymen.clear()
                    aymen.write(f"{turtle_leader} is the leader !", align="center", font=("Arial", 24, "normal"))
                screen.update()
                time.sleep(0.25)
        user_decision = screen.textinput("Again?", "Do you wish to play again ? type (yes/no)").lower()
        if user_decision == "yes":
            screen.clear()
            main()
        continue_playing = True
        screen.exitonclick()


if __name__ == "__main__":
    main()
