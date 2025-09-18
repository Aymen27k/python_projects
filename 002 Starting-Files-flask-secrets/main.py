import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

load_dotenv()
ACCESS_MAIL = os.getenv('ACCESS_MAIL')
ACCESS_PASSWORD = os.getenv('ACCESS_PASSWORD')

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(),
        validators.Email(message=('That\'s not a valid email address.'))])
    password = PasswordField(label='password', validators=[
        validators.DataRequired(),
        validators.Length(min=8, message=('Little short for an email address?')),
    ])
    submit = SubmitField(label="Log in")

app.secret_key = os.getenv('SECRET_KEY')


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == ACCESS_MAIL and password == ACCESS_PASSWORD:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template("login.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)