import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# Write your code below this line 👇

response = requests.get(URL)
data = response.text

soup = BeautifulSoup(data, 'html.parser')
movies = [item.getText() for item in soup.find_all('h3', class_='title')]
movie_parts = []
for movie_string in movies:
    if ')' in movie_string:
        parts = movie_string.split(')')
        movie_parts.append(parts)
    elif ':' in movie_string:  # Only try colon if parenthesis wasn't found
        parts = movie_string.split(':')
        movie_parts.append(parts)
    else:
        # Handle cases where neither delimiter is found, or log an error
        print(f"Warning: Could not split movie string: {movie_string}")
        continue


ranking_int = [int(item[0]) for item in movie_parts]
movie_names = [item[1].strip() for item in movie_parts]

final_movies = []
for movie in range(100):
    single_movie = f"{ranking_int[movie]}) {movie_names[movie]}"
    final_movies.append(single_movie)
final_movies.reverse()

with open("movies.txt", 'w', encoding="utf-8") as file:
    [file.write(line + "\n") for line in final_movies]

