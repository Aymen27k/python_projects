import requests
import os
from dotenv import load_dotenv
import datetime

current_datetime = datetime.datetime.now()
formatted_date = current_datetime.strftime("%Y%m%d")
print(formatted_date)

load_dotenv()

USERNAME = "aymen27k"
API_KEY = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"


pixel_post_param = {
    "date": formatted_date,
    "quantity": "1",
}

update_body = {
    "quantity": "5"
}

user_params = {
    "token": API_KEY,
    "username": "aymen27k",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_config = {
    "id": "graph1",
    "name": "Coding",
    "unit": "days",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": API_KEY,
}

#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# response = requests.post(url=post_pixel_endpoint, json=pixel_post_param, headers=headers)
# print(response.text)

response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(response.text)