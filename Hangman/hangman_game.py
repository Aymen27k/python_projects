import random
import hangman_words
import hangman_art
import os

incorrect_guesses = set()
all_guessed_letters = set()

# Pick a word randomly from a list
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)


# Clear the screen function.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Print the HangMan Logo
print(hangman_art.logo)
# Create blanks of the chosen Word.
display = ["_"] * word_length
print(display)

end_of_game = False
lives = 6
last_letter = ""

# Starting the game loop
while not end_of_game:
    index = 0
    letter_found = False

    # Getting user's Guess
    letter_input = input("Guess a letter : ").lower()
    clear_screen()
    # Check the input no longer than one letter and to be Alphanumeric.

    if len(letter_input) != 1 or not letter_input.isalpha():
        print(f"Make sure to type one Letter ! Please try again")
        continue

    # Check if the letter is not the same as previously entered.

    if letter_input in all_guessed_letters:
        print(f"You've entered this letter twice {letter_input} please chose another one !")
        continue

    all_guessed_letters.add(letter_input)
    # Logic that verifies the existence of the letter in the chosen word.
    for letter in range(word_length):
        if letter_input == chosen_word[index]:
            display[index] = letter_input
            letter_found = True

        index += 1

    if not letter_found:
        lives -= 1
        print(f"You've guessed {letter_input}. That's not in the word. You have {lives} lives remaining.")
        incorrect_guesses.add(letter_input)

    print("".join(display))
    if lives == 0:
        print(f"You lost! The word was {chosen_word}\n")
        print("Better luck Next time !")
        end_of_game = True
    if "_" not in display:
        end_of_game = True
        print("You won!")

    print(hangman_art.stages[lives])
