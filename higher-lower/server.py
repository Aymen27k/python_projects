from flask import Flask
import random

rnd_numb = random.randint(0,9)

app = Flask(__name__)

def comparing_result(function):
    def wrapper(*args, **kwargs):
        user_guess = function(*args, **kwargs)
        int_guess = int(user_guess)
        if rnd_numb < int_guess:
            return "<h1>You are too high</h1> \
        <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
        elif rnd_numb > int_guess:
            return "<h1>You are too low</h1> \
        <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
        else:
            return "<h1>You found the good number ! Congrats 👏🏼</h1>" \
            "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTN2NDU1Nmd3enA2ejFkZHVqZHdjNHh1NnVvOXlkZnNibGdnNDN0MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nbvFVPiEiJH6JOGIok/giphy.gif'>"
    return wrapper


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<number>")
@comparing_result
def compare(number):
    return number

if __name__ == "__main__":
    app.run(debug=True)
