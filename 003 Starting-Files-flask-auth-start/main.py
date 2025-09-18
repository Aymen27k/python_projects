import os
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from dotenv import load_dotenv
import secrets
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key= os.getenv("SECRET_KEY")

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)



# 🧠 User Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# 🧱 User Model
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(1000), nullable=False)

# 🏠 Home
@app.route('/')
def home():
    if current_user.is_authenticated:
        flash("You are already logged in, please logout to revisit the Home Page.")
        return redirect(url_for("secrets"))
    return render_template("index.html")

# 📝 Register
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")


        # Check if user already exists
        if User.query.filter_by(email=email).first():
            flash("Email already registered. Please log in.")
            return redirect(url_for("login"))

        # Create new user
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        new_user = User(email=email, name=name, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for("secrets"))

    return render_template("register.html")

# 🔐 Login
@app.route('/login', methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("The e-mail does not exist. please try again.")
            return redirect(url_for("login"))
        elif not check_password_hash(user.password, password):
            flash("Password incorrect, please try again.")
            return redirect(url_for("login"))

        login_user(user)
        return redirect(url_for("secrets"))
    return render_template("login.html")

# 🔒 Protected Route
@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)

# 🚪 Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("home"))

# 📥 Download (Protected)
@app.route('/download')
@login_required
def download():
    return send_from_directory("static/files", "cheat_sheet.pdf")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
