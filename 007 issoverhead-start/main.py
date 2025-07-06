import os

import dotenv
import requests
from datetime import datetime
import smtplib
import time
from dotenv import load_dotenv

dotenv.load_dotenv()

MY_LAT = 36.4384994
MY_LONG = 10.7210703
ISS_TRACKER_API = "http://api.open-notify.org/iss-now.json"
MY_MAIL = os.getenv("MY_MAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")



parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Africa/Tunis"
}


def check_position():
    response = requests.get(url=ISS_TRACKER_API)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5


def check_nighttime():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    return time_now.hour >= sunset or time_now.hour < sunrise


def main():
    while True:
        distance_conditions = check_position()
        night_condition = check_nighttime()
        print(f"Distance: {distance_conditions}")
        print(f"Night?: {night_condition}")
        if distance_conditions and night_condition:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_MAIL, MY_PASSWORD)
                connection.sendmail(from_addr=MY_MAIL,
                                    to_addrs="aymen27k@hotmail.com",
                                    msg=f"subject: ISS Close\n\nThe iss is passing by your location, please go check it out in the sky")
                print("Mail sent!")
        time.sleep(60)


if __name__ == "__main__":
    main()
