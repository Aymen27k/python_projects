# weather_fetcher.py
import os
from math import ceil
import requests


from dotenv import load_dotenv



load_dotenv()

API_KEY = os.getenv('API_KEY')
CITY = "Nabeul,TN"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather():
    try:      
        response = requests.get(URL)
        data = response.json()
        if data.get("cod") != 200:
            print(f"Error: {data.get('message')}")
            exit()

            # Extract and round values
        weather_data = {
            "temp": ceil(data["main"]["temp"]),
            "feels_like": ceil(data["main"]["feels_like"]),
            "humidity": ceil(data["main"]["humidity"]),
            "wind_speed_kmh": ceil(data["wind"]["speed"] * 3.6) , # Convert m/s to km/h
            "desc": data["weather"][0]["description"].capitalize()
        }
        # Display the simple scroll (as you designed it)
        print(f"📍 {CITY}")
        print(f"🌡️ Temp: {weather_data['temp']}°C (Feels like: {weather_data['feels_like']}°C)")
        print(f"💨 Wind: {weather_data['wind_speed_kmh']} km/h")
        print(f"💧 Humidity: {weather_data['humidity']}%")
        print(f"🌤️ Condition: {weather_data['desc']}")

        return weather_data
    except Exception as e:
        print("Error : Internet Offline or unavailable.")


def main():
    fetch_weather()


if __name__ == "__main__":
    main()
