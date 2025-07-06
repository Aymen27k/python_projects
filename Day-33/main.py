import requests
from requests import HTTPError
from datetime import datetime

SUNSET_SUNRISE_API = "https://api.sunrise-sunset.org/json"
ISS_TRACKER_API = "http://api.open-notify.org/iss-now.json"
PARAMETERS = {
    'lat': 36.43,
    'lng': 10.72,
    'formatted' : 0
}
time_now = datetime.now()
def sunset_sunrise():
    try:
        response = requests.get(url=SUNSET_SUNRISE_API, params=PARAMETERS)
        response.raise_for_status()
        parsed_response = response.json()
        sunrise = parsed_response["results"]["sunrise"].split("T")[1].split(":")[0]
        sunset = parsed_response["results"]["sunset"].split("T")[1].split(":")[0]
        print(time_now.hour)
        print(sunrise, sunset)
    except HTTPError as e:
        print(f"Error: {e}")
def iss_location():
    try:
        response = requests.get(url=ISS_TRACKER_API)
        response.raise_for_status()
        parsed_response = response.json()
        print(parsed_response)
        lat, long = parsed_response['iss_position']['latitude'], parsed_response['iss_position']['longitude']
        iss_position = (long, lat)
        print(lat, long)
    except HTTPError as e:
        print(f"Error: {e}")


def main():
    iss_location()
    sunset_sunrise()


if __name__ == "__main__":
    main()
