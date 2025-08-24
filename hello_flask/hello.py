from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper(*args, **kwargs):
        text = function()
        return f"<b>{text}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper(*args, **kwargs):
        text = function()
        return f"<em>{text}</em>"
    return wrapper

def make_underlined(function):
    def wrapper(*args, **kwargs):
        text = function()
        return f"<u>{text}</u>"
    return wrapper

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
    '<p>This is my website</p>' \
    '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmxhdGJqY296NzBhcXgwMXNoYnFuODMwNWNyeDVybGJ4YXljYTAzciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Cz6TlrRVVyv9S/giphy.gif">'

@app.route("/bye")
@make_emphasis
@make_bold
@make_underlined
def bye():
    return '<h1 style="text-align: center">Bye!</h1>'

@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}😎"

if __name__ == "__main__":
    app.run(debug=True)
