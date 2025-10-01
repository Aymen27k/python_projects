from datetime import datetime
from dotenv import load_dotenv
import os
from flask import Flask, render_template, redirect, url_for
from database import db
from models import Ritual, User
from ritual_form import RitualForm
from auth_routes import auth
from flask_login import LoginManager, login_required, current_user, logout_user


load_dotenv()

# Creating the flask app and configuring it
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRES_URL")
db.init_app(app)
app.register_blueprint(auth)

# creating loginManager
login_manager = LoginManager()
login_manager.init_app(app)

# 🧠 User Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


with app.app_context():
    db.create_all()
# Home Route 
@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for('user_hub'))
    return render_template ("index.html")

@app.route("/user_hub")
@login_required
def user_hub():
    return render_template("user_hub.html")

# Creating the Form and sending it to the front, Once submitted it get added to the Database
@app.route("/add", methods=['GET','POST'])
@login_required
def add_ritual():
    form = RitualForm()
    if form.validate_on_submit():
        session_start = form.begin_time.data.strip()
        session_end = form.finish_time.data.strip()
        extra_comment = form.comment.data.strip()
        date = datetime.now().strftime("%d %B, %Y")
        new_ritual = Ritual(user_id=current_user.id,date=date, begin_time=session_start, finish_time=session_end,comment=extra_comment)
        db.session.add(new_ritual)
        db.session.commit()
        return redirect(url_for('user_hub'))
    return render_template("add_ritual.html", form=form)

# Loading Rituals from Database and sending them to the front for display
@app.route("/view_rituals")
@login_required
def view_rituals():
    result = db.session.execute(db.select(Ritual).where(Ritual.user_id == current_user.id).order_by(Ritual.date))
    all_rituals = result.scalars().all()
    return render_template("view_rituals.html", rituals=all_rituals)

# Deleting the selected ritual and refreshing the view ritual page
@app.route("/delete/<int:ritual_id>")
@login_required
def delete_ritual(ritual_id):
    ritual_to_delete = db.session.query(Ritual).filter_by(
    id=ritual_id,
    user_id=current_user.id
).first_or_404()
    db.session.delete(ritual_to_delete)
    db.session.commit()
    return redirect(url_for('view_rituals'))

# Editing the selected ritual by loading it in a new form and submitting the change to the Database
@app.route("/edit_ritual/<int:ritual_id>", methods=['GET','POST'])
@login_required
def edit_ritual(ritual_id):
    ritual_to_edit = db.session.query(Ritual).filter_by(
    id=ritual_id,
    user_id=current_user.id
).first_or_404()

    form = RitualForm(obj=ritual_to_edit)

    if form.validate_on_submit():
        ritual_to_edit.date = datetime.now().strftime("%d %B, %Y")
        ritual_to_edit.begin_time = form.begin_time.data
        ritual_to_edit.finish_time = form.finish_time.data
        ritual_to_edit.comment = form.comment.data
        db.session.commit()
        return redirect(url_for('view_rituals'))
    return render_template("edit_ritual.html", form=form, ritual_id=ritual_id)

# Starting point of the Flask Server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)
