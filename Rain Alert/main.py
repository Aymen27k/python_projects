import json
import os

import requests
import smtplib
from dotenv import load_dotenv

load_dotenv()

MY_MAIL = "ethancarter123x@gmail.com"
password = "kyjlvbfzmdhxcbgh"
api = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.getenv("api_key")
parameters = {
    "lat": 36.451832,
    "lon" : 10.735150,
    "appid" : api_key,
    "exclude" : "current,minutely,daily,alerts"
}

try:
    with open("data.json", "r") as file:
        weather_data = json.load(file)
    print(weather_data)
except Exception as e:
    print(f"Error occurred {e}")

id_slice = weather_data['hourly'][0]['weather'][0]['id']

new_12_hour_forecast = weather_data['hourly'][:12]

condition_codes = [hour_data['weather'][0]['id'] for hour_data in new_12_hour_forecast]

is_gonna_rain = False
for id in condition_codes:
    if int(id) < 700:
        is_gonna_rain = True
    if is_gonna_rain:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_MAIL,password)
            connection.sendmail(to_addrs=MY_MAIL, from_addr=MY_MAIL, msg="subject:Rain Alert \n\n It's going to rain Soon!")
            print("Mail Sent")
            break
