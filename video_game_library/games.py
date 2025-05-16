class Game:
    def __init__(self, title, developer, year):
        self.title = title
        self.developer = developer
        self.year = year


class GameLibrary:
    def __init__(self):
        self.games = []  # Initialize an empty list to store Game objects

    def add_game(self, game):
        self.games.append(game)

    def find_game_by_developer(self, developer):
        result = []
        for game in self.games:
            if game.developer == developer:
                result.append(game)
        return result

    def sort_games_by_year(self):
        result = []
        for game in self.games:
            if 2010 <= game.year <= 2020:
                result.append(game)
        return result

    def display_all_games(self):
        output = ""
        for game in self.games:
            print(f"Title: {game.title}, Developer {game.developer}, Year: {game.year}")
            output += f"Title: {game.title}, Developer {game.developer}, Year: {game.year}\n"
        return output


# Creating game objects
game1 = Game("The witcher 3", "CD Projekt Red", 2015)
game2 = Game("Cyberpunk 2077", "CD Projekt Red", 2020)
game3 = Game("God of War", "Santa Monica Studio", 2018)

# Creating a GameLibrary object
library = GameLibrary()

# Add games to the library
library.add_game(game1)
library.add_game(game2)
library.add_game(game3)

cdpr_games = library.find_game_by_developer("CD Projekt Red")
for game in cdpr_games:
    print(game.title)

game_year_sorting = library.sort_games_by_year()
for game in game_year_sorting:
    print(f"Games released between 2010 & 2020: {game.title}")

# Display all games
library.display_all_games()

with open("Game Library.txt", "w") as file:
    file.write(library.display_all_games())
