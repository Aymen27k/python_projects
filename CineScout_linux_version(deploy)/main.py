import os
import json
from datetime import datetime
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium_fetcher import get_html


script_dir = os.path.dirname(os.path.abspath(__file__))
URL = "https://1337x.to/popular-movies"
match = []
ENV_FILE_PATH = os.path.join(script_dir, '.env')
load_dotenv(dotenv_path=ENV_FILE_PATH)
MAIL_ADDRESS = os.getenv("BOT_MAIL")
PASSWORD = os.getenv("PASSWORD")
DESTINATION = os.getenv("DESTINATION_MAIL")
WATCHLIST_PATH = os.path.join(script_dir, 'watchlist.json')
NOTIFIED_MOVIES_PATH = os.path.join(script_dir, 'notified_movies.json')
LOG_PATH = os.path.join(script_dir, 'cron_output.log')


# ------------- Scraping Torrent website for last movies Titles ----------------#
def scrap_movies(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    movies_full_title = soup.select('a[href^="/torrent/"]')
    movie_title = [tag.get_text(strip=True) for tag in movies_full_title]
    return movie_title


def reading_json(path):
    try:
        with open(path, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecoder):
        return []
    finally:
        return data


def find_matches():
    global match
    html_text = get_html(URL)
    available_movies = scrap_movies(html_text)

    if not available_movies:
        # Explicitly log failure case
        log_to_cron_output("⚠️ No movies scraped — possible fetch or parse issue.")
        return [], available_movies

    wanted_movies = reading_json(WATCHLIST_PATH)
    already_notified = reading_json(NOTIFIED_MOVIES_PATH)

    for title in available_movies:
        title_lower = title.lower()
        if any(wanted.lower() in title_lower for wanted in wanted_movies['movies']):
            if any(res.lower() in title_lower for res in wanted_movies['preferred_qualities']):
                if title not in already_notified["movies"]:
                    match.append(title)

    return match, available_movies


def saving_notified_movies(new_matches, file_path=NOTIFIED_MOVIES_PATH):
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
        
        \n{formatted_titles}

        Enjoy your binge, maestro. CineScout’s always watching. 👁️🕊️
        — CineScout v2.0
        """)
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MAIL_ADDRESS, PASSWORD)
                connection.send_message(msg)
                saving_notified_movies(movies_list)
                print(f"Mail sent successfully! to => {DESTINATION}")
                log_to_cron_output(f"Mail sent successfully! to => {DESTINATION}")
        except Exception as e:
            print(f"Failed to send email: {e}")
    else:
        print("🚫 No matches today — no email sent.")


def log_to_cron_output(message: str, log_file=LOG_PATH):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as f:
        f.write(f'[{timestamp}] {message}\n')


def main():
    log_to_cron_output("CineScout has been launched")
    matched_movies, available_movies = find_matches()

    if not available_movies:
        # Already logged inside find_matches
        return

    if matched_movies:
        mail_sender(matched_movies)
    else:
        log_to_cron_output("ℹ️ No matches found today.")



if __name__ == "__main__":
    main()
