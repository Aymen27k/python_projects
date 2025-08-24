from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

app.secret_key = "your-super-secret-key-that-is-hard-to-guess"


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)