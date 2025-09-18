from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, redirect, url_for, request, flash
from database import db
from models import User


auth = Blueprint('auth',__name__)

# 📝 Register
@auth.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")

        # In case where the User is already registered in the DB
        if User.query.filter_by(email=email).first():
            flash("Email already registered. Please log in.")
            return redirect(url_for("auth.login"))
        
        hashed_password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
        new_user= User(email=email, name=name, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for("user_hub"))
    return render_template("/register.html")

# 🪪 Login
@auth.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("The e-mail does not exist, please try again.")
            return redirect(url_for("auth.login"))
        elif not check_password_hash(user.password, password):
            flash("Password incorrect, please try again")
            return redirect(url_for("auth.login"))
        login_user(user)
        return redirect(url_for("user_hub"))
    return render_template("/login.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("home"))