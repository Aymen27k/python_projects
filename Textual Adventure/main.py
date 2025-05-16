inventory = []


def start_room():
    print("You find yourself in a dark and mysterious room.")
    print("There are two doors : one to the north and one to the east.")
    print("You see a Shiny sword on the ground.")
    choice = input("What is your next move? (North/east/take sword)").lower()
    if choice == "north":
        forest()
    elif choice == "east":
        cave()
    elif choice == "take sword":
        inventory.append("sword")
        print("You've picked up the Sword")
        start_room()
    else:
        print("Invalid choice, Try again.")
        start_room()


def forest():
    print("You are now in a dense forest")
    print("There is a path to the west, and back to the south")
    choice = input("Which parth will you take? (west/south)").lower()
    if choice == "west":
        treasure_room()
    elif choice == "south":
        start_room()
    else:
        print("Invalid choice, try again.")
        forest()


def cave():
    print("You enter a dark cave")
    print("There is a tunnel going north and back to the west")
    choice = input("Which tunnel will you take? (north/west)").lower()
    if choice == "north":
        monster_room()
    elif choice == "west":
        start_room()
    else:
        print("Invalid choice, try again.")
        cave()


def treasure_room():
    print("you found a room with a treasure chest!")
    print("you won the game!")


def monster_room():
    print("You're in front of a monster!")
    if "sword" in inventory:
        choice = input("Do you want to use your sword? (yes/no)").lower()
        if choice == "yes":
            print("You slay the monster into Pieces with your Sword!")
            treasure_room()
    else:
            print("The monster overpower you and ate you alive!")
            print("Game Over!")


start_room()

