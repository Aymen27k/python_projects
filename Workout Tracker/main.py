from dotenv import load_dotenv
import os
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

load_dotenv()
# ------------- Nutritionix Variables --------------------#
api_id = os.getenv("NUTRITIONIX_API_ID")
api_key = os.getenv("NUTRITIONIX_API_KEY")
HOST_DOMAIN = "https://trackapi.nutritionix.com"
NLP_ENDPOINT = "/v2/natural/exercise"

nlp_header = {
    "x-app-id": api_id,
    "x-app-key": api_key,
}
SS_POST_ENDPOINT_URL = os.getenv("SS_POST_ENDPOINT")
SS_GET_ENDPOINT_URL = os.getenv("SS_GET_ENDPOINT")

SHEETY_UN = os.getenv("SHEETY_USERNAME")
SHEETY_AUTH = os.getenv("SHEETY_AUTH")
SHEETY_SECRET_TOKEN = os.getenv("SHEETY_SECRET_TOKEN")

AUTH_VALUE = HTTPBasicAuth(SHEETY_UN, SHEETY_AUTH)
headers = {
    "Authorization": f"Bearer {SHEETY_SECRET_TOKEN}"
}
current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%d/%m/%Y")

formatted_time = current_datetime.strftime("%H:%M:%S")


def extract_data(json_data):
    extracted_duration = json_data['exercises'][0]['duration_min']
    extracted_calories = json_data['exercises'][0]['nf_calories']
    extracted_exercise_name = json_data['exercises'][0]['name'].title()
    print(
        f"Duration: {extracted_duration}, Calories_Burned: {extracted_calories}, Exercise Name: {extracted_exercise_name}")
    return extracted_duration, extracted_calories, extracted_exercise_name


def get_users_input():
    print("Welcome to Aymen's Workout Tracker")
    user_query = input("Tell me which exercise you did: ").lower()
    return user_query


user_input = get_users_input()


def nlp_post_request(query):
    response = requests.post(f"{HOST_DOMAIN}{NLP_ENDPOINT}", headers=nlp_header, json=query)
    response.raise_for_status()
    nlp_data = response.json()
    return nlp_data


query = {
    "query": user_input
}
nlp_response = nlp_post_request(query)

duration, calories, exercise = extract_data(nlp_response)
sheety_post_body = {
    "myWorkout": {
        "date": formatted_date,
        "time": formatted_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

print(f'Username: {SHEETY_UN}\nPassword: {SHEETY_AUTH}')
try:
    response = requests.post(SS_POST_ENDPOINT_URL, json=sheety_post_body, headers=headers)
    response.raise_for_status()
    print("Workout Added!")
except Exception as e:
    print(f"Something went wrong: {e}")

