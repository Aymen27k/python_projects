import random
import art
import game_data
import os

print("Created with passion ♥ by Aymen Kalaï Ezar. Copyright © 2025. All Rights Reserved.")
# Logo printing
print(art.logo)


# Generate a celebrity and construct a presentation sentence
def generate_celeb():
    celeb = random.choice(game_data.data)
    return celeb


def print_celeb(celeb, letter):
    name = celeb['name']
    description = celeb['description']
    country = celeb['country']
    print(f"Compare {letter}: {name}, a {description}, from {country}")


# Comparing two followers_counts and returning the right_answer
def higher_celeb(followers_a, followers_b):
    if followers_a > followers_b:
        return 'a'
    else:
        return 'b'


def result(right_answer, user_guess, player_score):
    if right_answer == user_guess:
        player_score += 1
        print(f"You're right ! Current score: {player_score}")
        return False, player_score
    else:
        print(f"Sorry, that's wrong. Final score: {player_score}")
        return True, player_score


def update_high_score(current_score, high_score):
    if current_score > high_score:
        high_score = current_score
        print(f"A NEW HIGH SCORE ! {high_score}")
    elif current_score != 0:
        print(f"No new High score ! high Score to Beat {high_score}")
    return high_score


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Ask the user Which celebrities has more Followers 'A' or 'B' ?


def higher_lower():
    celeb_a = generate_celeb()
    game_over = False
    score = 0
    while not game_over:
        print_celeb(celeb_a, 'A')
        followers_a = celeb_a['follower_count']
        print(art.vs)
        celeb_b = generate_celeb()
        followers_b = celeb_b['follower_count']
        print_celeb(celeb_b, 'B')
        guess = input("Who has more Followers? Type 'A or 'B': ").lower()
        right_answer = higher_celeb(followers_a, followers_b)
        game_over, score = result(right_answer, guess, score)
        if not game_over:
            celeb_a = celeb_b
    return score, game_over


def main():
    continue_playing = False
    current_high_score = 0
    score, game_over = higher_lower()
    current_high_score = update_high_score(score, current_high_score)

    while not continue_playing:
        if game_over:
            retry = input("Would you like to try again ? Type 'Y' or 'N' ").lower()
            if retry == 'y':
                score, game_over = higher_lower()
                current_high_score = update_high_score(score, current_high_score)
            else:
                continue_playing = True


if __name__ == "__main__":
    main()
