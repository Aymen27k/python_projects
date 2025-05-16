import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
# Storing the ASCII art in a dictionary
images = [rock, paper, scissors]


def get_user_choice():
    while True:
        try:
            user_choice = int(input("Please make a choice : 0 for Rock,1 for Paper and 2 for Scissors \n"))
            if 0 <= user_choice <= 2:
                return user_choice
            else:
                print("Invalid choice. Please try again...")
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")


def get_computer_choice():
    computer_choice = random.randint(0, 2)
    return computer_choice


def display_choices(user_choice, computer_choice):
    print("User's Choice : ")
    print(images[user_choice])
    print("Computer's Choice : ")
    print(images[computer_choice])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a Draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win !")
    elif user_choice == 2 and computer_choice == 1:
        print("You Win !")
    elif user_choice == 1 and computer_choice == 0:
        print("You Win !")
    else:
        print("You lose !")


def main():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        play_again = input("Do you want to play again ? (y/n) : \n").lower()
        if play_again != "y":
            print("Thank for playing my game ~ Made with ♥ by Aymen Kalaï Ezar")
            break


if __name__ == "__main__":
    main()

# This is the liner way of making it
# user_choice = int(input("0 to Chose Rock,1 to chose Paper and 2 to chose Scissors \n"))
# if user_choice >= 3 or user_choice < 0:
#     print("Invalid choice. Please try again with rock, paper or scissors")
# else:
#     print("User's choice : ")
#     print(images[user_choice])
#     computer_choice = random.randint(0, 2)
#     print("Computer choice : ")
#     print(images[computer_choice])
# if user_choice == computer_choice:
#     print("It's a Draw")
# elif user_choice == 0 and computer_choice == 2:
#     print("You Win !")
# elif user_choice == 2 and computer_choice == 1:
#     print("You Win !")
# elif user_choice == 1 and computer_choice == 0:
#     print("You Win !")
# else:
#     print("You lose !")
