from art import logo
import random
import os

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_playing = False
credit = 1000


############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def draw_cards(num_card=2):
    hand = []
    for x in range(num_card):
        index = random.randint(0, 11)
        hand.append(CARDS[index])
    return hand


def hand_value(hand):
    hand_total = 0
    ace_count = 0
    bust = False
    for card in hand:
        hand_total += card
        if card == 11:
            ace_count += 1
    while hand_total > 21 and ace_count > 0:
        if 11 in hand:
            index_of_ace = hand.index(11)
            hand[index_of_ace] = 1
            hand_total -= 10
            ace_count -= 1
    if hand_total > 21:
        bust = True
    return hand_total, bust


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_game_status(player_hand, player_total, computer_first_card):
    print(f"Your Cards: {player_hand}, current score: {player_total}")
    print(f"Computer's first card :{computer_first_card}")


def display_final_game(player_hand, player_total, player_credit, computer_hand, computer_total):
    print(f"You have {player_credit} tokens")
    print(f"Your Final hand: {player_hand}, final score {player_total} ")
    print(f"Computer final hand: {computer_hand}, final score: {computer_total}")


# Final winning Condition Check
def who_win(player, player_credit, computer):
    if player > computer:
        print("You win 🎉")
        player_credit += 200
        print(f"You have won 200 Tokens, Your total is {player_credit}")
        return player_credit
    elif player == computer:
        print("Its a draw 🙃")
    else:
        print("You lose 🤬")


# Check BlackJack Winning condition
def blackjack_win(player_hand, player_total, computer_hand, computer_total):
    game_over = True
    player_hand_length = len(player_hand)
    computer_hand_length = len(computer_hand)
    if (player_total == 21 and player_hand_length == 2) and (computer_total == 21 and computer_hand_length == 2):
        print("Two Blackjacks ! It's a DRAW 🤝🏻")
        return game_over
    elif player_total == 21 and player_hand_length == 2:
        print("BlackJack 🤩 You win")
        return game_over
    elif computer_total == 21 and computer_hand_length == 2:
        print("BlackJack 🤩 Dealer Win")
        return game_over


# Main Game Logic
def blackjack(credit):
    player_hit = True
    dealers_hit = True
    game_over = False
    if start_game == 'y':
        print(logo)
        player_hand = draw_cards()
        computer_hand = draw_cards()
        computer_first_card = computer_hand[0]
        player_total = hand_value(player_hand)[0]
        computer_total = hand_value(computer_hand)[0]
        display_game_status(player_hand, player_total, computer_first_card)
        game_over = blackjack_win(player_hand, player_total, computer_hand, computer_total)
        if game_over:
            display_final_game(player_hand, player_total, credit, computer_hand, computer_total)
            player_hit = False
            dealers_hit = False

    # Player Turn
    while player_hit:
        next_decision = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if next_decision == 'y':
            player_hand.append(draw_cards(num_card=1)[0])
            player_total, player_busted = hand_value(player_hand)
            display_game_status(player_hand, player_total, computer_first_card)
            if player_busted:
                display_final_game(player_hand, player_total, credit, computer_hand, computer_total)
                print("You went over. You lose 😬")
                player_hit = False
                game_over = True
        else:
            player_hit = False
    if not game_over:
        # Dealer's Turn
        while dealers_hit:
            computer_total = hand_value(computer_hand)[0]
            if computer_total < 17:
                computer_hand.append(draw_cards(num_card=1)[0])
                computer_total, computer_busted = hand_value(computer_hand)
                if computer_busted:
                    display_final_game(player_hand, player_total, credit, computer_hand, computer_total)
                    print("Computer went over. You Win 🎉")
                    dealers_hit = False
                    game_over = True
            else:
                dealers_hit = False

    # Final score comparison
    if not game_over:
        display_final_game(player_hand, player_total, credit, computer_hand, computer_total)
        who_win(player_total, computer_total, credit)


print("Created with passion ♥ by Aymen Kalaï Ezar. Copyright © 2025. All Rights Reserved.")
while not continue_playing and credit != 0:
    start_game = input("Do you want to play a game of Blackjack? type 'y' or 'n': ").lower()
    if start_game == 'y':
        credit -= 200
        clear_screen()
        blackjack(credit)
    else:
        continue_playing = True
if credit == 0:
    print("You've lost all your credits! Game Over")
