from flask import Flask
from flask import render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

random_number = random.randint(0,10)
actual_year = datetime.now().year
GENDERIZE_URL = "https://api.genderize.io"
AGIFY_URL = "https://api.agify.io"
POSTS_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_api(url, api_param):
    response = requests.get(url, params=api_param)
    response.raise_for_status()
    data = response.json()
    return data

@app.route("/")
def home():
    return render_template('index.html', number = random_number, year = actual_year )

@app.route("/guess/<user_name>")
def guess(user_name):
    USER_PARAM = {'name' : user_name}
    gender_data = fetch_api(GENDERIZE_URL, USER_PARAM)
    age_data = fetch_api(AGIFY_URL, USER_PARAM)
    entered_name = user_name.title()
    user_gender = gender_data['gender']
    user_age = age_data['age']
    return render_template('guess.html', name = entered_name, gender = user_gender, age = user_age)

@app.route("/blog")
def get_blog():
    all_posts = fetch_api(POSTS_URL, {})
    return render_template("blog.html", posts = all_posts)




if __name__ == "__main__":
    app.run(debug=True)
