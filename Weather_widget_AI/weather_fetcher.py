# weather_fetcher.py
import os
from math import ceil
import requests
import datetime
from google import genai
from dotenv import load_dotenv
import notify2
import time


notify2.init("Weather Report")

load_dotenv()

API_KEY = os.getenv('API_KEY')
CITY = "Nabeul,TN"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def summarize_weather(data_dict):
    """Calls the Gemini API to summarize the weather data."""
    with genai.Client() as client:
        time_of_day = datetime.datetime.now().strftime("%H:%M")

        # Prompt
        prompt = f"""
        Act as a weather newscaster for a terminal utility.
        Summarize the following raw weather data into a short, engaging, single paragraph (maximum 3 sentences).
        Do not use lists or bullet points. Start with a greeting me by my name "Aymen".

        RAW DATA:
        - Current Time: {time_of_day}
        - Location: {CITY}
        - Temperature: {data_dict['temp']}°C
        - Feels Like: {data_dict['feels_like']}°C
        - Conditions: {data_dict['desc']}
        - Wind: {data_dict['wind_speed_kmh']} km/h
        - Humidity: {data_dict['humidity']}%
        """

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            
            # Display notification of the Weather Summary
            print(response.text)
            n = notify2.Notification("🌤️ Weather Update", response.text)
            n.set_timeout(10000)
            n.show()
            time.sleep(1)

        except Exception as e:
            print(f"\nError: Could not get AI summary. Check API Key or internet connection. Details: {e}")

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
        """ # Display the simple scroll (as you designed it)
        print(f"📍 {CITY}")
        print(f"🌡️ Temp: {weather_data['temp']}°C (Feels like: {weather_data['feels_like']}°C)")
        print(f"💨 Wind: {weather_data['wind_speed_kmh']} km/h")
        print(f"💧 Humidity: {weather_data['humidity']}%")
        print(f"🌤️ Condition: {weather_data['desc']}") """

        return weather_data
    except Exception as e:
        print("Error : Internet Offline or unavailable.")


def main():
    weather_data = fetch_weather()
    if weather_data:
        summarize_weather(weather_data)

if __name__ == "__main__":
    main()
