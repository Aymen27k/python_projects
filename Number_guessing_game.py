import random


logo = r'''

 _____                    _____ _          _   _                 _               
|  __ \                  |_   _| |        | \ | |               | |              
| |  \/_   _  ___  ___ ___ | | | |__   ___|  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __|| | | '_ \ / _ \ . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \| | | | | |  __/ |\  | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/\_/ |_| |_|\___\_| \_/\__,_|_| |_| |_|_.__/ \___|_|                   

'''

NUMBER_TO_GUESS = random.randint(1, 100)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()


# The function that compare the guesses with the right number
def guessing_number(difficulty):
    guessed_number = False
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    while not guessed_number and attempts > 0:
        print(f"You have {attempts} remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
            if guess < 0 or guess > 100:
                print("Your guess must be between 1 and 100.")
                continue
            if guess == NUMBER_TO_GUESS:
                print(f"You got it! The answer was {NUMBER_TO_GUESS}")
                guessed_number = True
            elif guess > NUMBER_TO_GUESS:
                print("Too high.")
                print("Guess Again.")
                attempts -= 1
            else:
                print("Too Low.")
                print("Guess Again.")
                attempts -= 1
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if attempts == 0:
            print("You've run out of guesses, you lose")


guessing_number(difficulty_level)
