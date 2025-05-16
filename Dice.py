import random


def get_target_roll():
    while True:
        try:
            target = int(input("Pick a number from 1 to 6."))
            if 1 <= target <= 6:
                return target
            else:
                print("Invalid number. Please pick a number from 1 to 6.")
        except ValueError:
            print("Invalid input, please enter a number")


def roll_dice(target):
    roll = 0
    number_of_rolls = 0
    while roll != target:
        number_of_rolls += 1
        roll = random.randint(1, 6)
        print(f"You rolled {roll}")
    print(f"You finally rolled a {target}")
    print(f"It took you {number_of_rolls} time(s)")


target_roll = get_target_roll()
roll_dice(target_roll)

