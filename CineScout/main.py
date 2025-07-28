import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

URL = "https://1337x.to/popular-movies"
match = []
MAIL_ADDRESS = os.getenv("MAIL")
PASSWORD = os.getenv("PASSWORD")
DESTINATION = os.getenv("DESTINATION_MAIL")


# ------------- Scrapping Torrent website for last movies Titles ----------------#
def scrap_movies():
    response = requests.get(URL)
    data = response.text

    soup = BeautifulSoup(data, 'html.parser')
    movies_full_title = soup.select('a[href^="/torrent/"]')
    movie_title = [tag.get_text(strip=True) for tag in movies_full_title]
    return movie_title


def reading_json(path):
    try:
        with open(path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"⚠️ File not found: {path}")
        data = []
    except json.JSONDecodeError:
        print(f"⚠️ JSON decoding failed for: {path}")
        data = []
    except PermissionError:
        print("🚫 Permission denied when reading watchlist.json")
        data = []
    return data


def find_matches():
    global match
    available_movies = scrap_movies()
    wanted_movies = reading_json("watchlist.json")
    already_notified = reading_json("notified_movies.json")
    for title in available_movies:
        title_lower = title.lower()
        if any(wanted.lower() in title_lower for wanted in wanted_movies['movies']):
            if any(res.lower() in title_lower for res in wanted_movies['preferred_qualities']):
                if title not in already_notified["movies"]:
                    match.append(title)
    return match


def saving_notified_movies(new_matches, file_path="notified_movies.json"):
    try:
        data = reading_json(file_path)
        already_notified = data.get("movies", [])
    except (FileNotFoundError, json.JSONDecodeError):
        already_notified = []
    updated_list = list(set(already_notified + new_matches))

    # Write updated list back to file
    with open(file_path, "w") as file:
        json.dump({"movies": updated_list}, file, indent=2)


def mail_sender(movies_list):
    if movies_list:
        timestamp = datetime.now().strftime("%B %d, %Y — %H:%M")
        formatted_titles = "\n".join([f"• {title}" for title in movies_list])
        msg = EmailMessage()
        msg["Subject"] = f"🎬 CineScout Match Report — {timestamp}"
        msg["From"] = MAIL_ADDRESS
        msg["To"] = DESTINATION
        msg.set_content(f"""
        Hey Aymen! 🚀

        Your movie radar just picked up some fresh matches based on your wishlist and preferred quality:
        
        {formatted_titles}

        Enjoy your binge, maestro. CineScout’s always watching. 👁️🕊️
        — CineScout v1.0
        """)
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MAIL_ADDRESS, PASSWORD)
                connection.send_message(msg)
                saving_notified_movies(movies_list)
                print(f"Mail sent successfully! to => {DESTINATION}")
        except Exception as e:
            print(f"Failed to send email: {e}")
    else:
        print("🚫 No matches today — no email sent.")


def main():
    matched_movies = find_matches()
    # print(f"Scrapped Movies: {available_movies}")
    # print(f"Wanted Movies: {wanted_movies}")
    # print(f"Here the matched movies found : {matched_movies}")
    mail_sender(matched_movies)


if __name__ == "__main__":
    main()
