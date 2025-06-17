import turtle
import pandas

screen = turtle.Screen()
screen.title("Name the State")
screen.setup(725, 491)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
game_is_on = True

guessed_states = []
while game_is_on:
    player_answer = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What's the next State?").title()
    states_data = pandas.read_csv("50_states.csv")
    state_names = states_data.state
    result = state_names.str.contains(player_answer)
    # Checking if the guess is correct
    if result.any():
        my_df = states_data[states_data["state"] == player_answer]
        x = my_df['x'].item()
        y = my_df['y'].item()
        writer.goto(x, y)
        writer.write(player_answer)
        # Adding the correct guessed state to a list
        if player_answer in guessed_states:
            pass
        else:
            guessed_states.append(player_answer)
        pass
    else:
        pass
    # Winning Condition, ending the Loop if All States guessed
    if len(guessed_states) == 50:
        game_is_on = False
    # Exit the game
    if player_answer == "Exit":
        missed_states = -state_names.isin(guessed_states)
        name_missed_states = states_data[missed_states]
        pandas.DataFrame.to_csv(name_missed_states.state, "missing_state.csv", index=False)
        break

screen.exitonclick()
