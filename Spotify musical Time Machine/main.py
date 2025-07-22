from bs4 import BeautifulSoup
import requests
from datetime import datetime
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

load_dotenv()
good_date_format = False
SPOTIFY_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")
REDIRECT_URI = "http://127.0.0.1:8888/callback"
song_title = []
artist_name = []
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private playlist-modify-public"))

while not good_date_format:
    try:
        date_input = input("Which year would you like to travel to ? Type a date in this format YYYY-MM-DD: ")
        valid_date = datetime.strptime(date_input, "%Y-%m-%d")
        good_date_format = True
    except ValueError:
        print("You entered a wrong date format, please try again with -> YYYY-MM-DD <-Format")
        continue

URL = f"https://www.billboard.com/charts/hot-100/{date_input}/"

response = requests.get(URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")
song_title = [item.get_text(strip=True) for item in soup.select("h3.a-no-trucate")]
artist_name = [artist.get_text(strip=True) for artist in soup.select("span.a-no-trucate")]
cleaned_up_artist_name = [item.replace("Featuring", "feat.").strip() for item in artist_name]

billboard_100 = list(zip(song_title, cleaned_up_artist_name))
#print(billboard_100)
#print(sp.me()["display_name"])

# ---------- Extracting the year of the playlist ---------------#
date_obj = datetime.strptime(date_input, "%Y-%m-%d")
year = date_obj.year
# --------------- Forming queries ------------------------#
song_uri = []
for song, artist in billboard_100:
    query = f"track:{song} artist:{artist}"
    minimal_query = f"track:{song} year:{year}"
    try:
        result = sp.search(q=query, type="track", limit=1)
        uri = result["tracks"]["items"][0]["uri"]
    except IndexError:
        print(f"Primary query failed. Trying minimal query...\n→ {query}")
        try:
            result = sp.search(q=minimal_query, type="track", limit=1)
            uri = result["tracks"]["items"][0]["uri"]
        except IndexError:
            print(f"Fallback also failed: {minimal_query}")
            uri = None
    if uri:
        song_uri.append(uri)

# --------------- Creating Playlist -------------------#
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user_id, f"{len(song_uri)} Songs - {year} Billboard", public=True)
playlist_id = playlist["id"]
playlist_url = playlist["external_urls"]["spotify"]
sp.playlist_add_items(playlist_id, song_uri)

# ----------------- Delivering the Playlist ---------------#
print("✅ Playlist created and filled!")
print(f"🎧 Check it out: {playlist_url}")
