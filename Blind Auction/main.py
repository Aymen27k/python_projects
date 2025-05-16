import os
from art import logo

continue_bidding = True
all_bids = {}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


print(logo)
print("Welcome to the secret auction program.")

while continue_bidding:
    more_bid = ""
    bidder_name = input("What's your name?: ")
    bid_value = int(input("What's your bid?: $"))
    all_bids[bidder_name] = bid_value
    more_bid = input("Are there any other bidders? Type 'Yes' or 'no'").lower()
    clear_screen()
    if more_bid != "yes":
        find_highest_bid(all_bids)
        continue_bidding = False
        print("Goodbye")
