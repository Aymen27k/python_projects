from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', name="", password="")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        first_name = request.form["name"]
        password = request.form["password"]
        return render_template('index.html', name= first_name, password=password)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
