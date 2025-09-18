import csv
import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime

FILE_PATH = 'rituals.csv'
load_dotenv()
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

def save_data_to_csv(data):
    """_summary_
    This function takes the data from the front end and save it on a csv file.
    """    
    # Check if the file already exists.
    file_exists = os.path.isfile(FILE_PATH)
    
    # Open the file in append mode.
    with open(FILE_PATH, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # If the file didn't exist, write the headers first.
        if not file_exists:
            writer.writerow(['date','begin_time', 'finish_time', 'comment'])
            print("New CSV file created with data!")
            
        # Write the data row.
        writer.writerow(data)
        print("Data appended to CSV file.")


class RitualForm(FlaskForm):
    begin_time = StringField('Begin Time', validators=[DataRequired()], render_kw={"placeholder": "When the session start? (e.g., 8:00)"})
    finish_time = StringField('Finish Time', validators=[DataRequired()], render_kw={"placeholder": "When the session end? (e.g., 17:20)"})
    comment = TextAreaField('Additional comment', render_kw={"placeholder": "Enter any comment here ..."})
    submit = SubmitField('Submit')
    

    def validate_begin_time(self, begin_time):
        try:
            datetime.strptime(begin_time.data, '%H:%M')
        except ValueError:
            raise ValidationError('Invalid time format. Please use H:MM (e.g., 8:30)')
    def validate_finish_time(self, finish_time):
        try:
            datetime.strptime(finish_time.data, '%H:%M')
        except ValueError:
            raise ValidationError('Invalid time format. Please use H:MM (e.g., 17:00)')

@app.route("/")
def home():
    return render_template ("index.html")

@app.route("/add", methods=['GET','POST'])
def add_ritual():
    form = RitualForm()
    if form.validate_on_submit():
        session_start = form.begin_time.data
        session_end = form.finish_time.data
        extra_comment = form.comment.data
        date = datetime.now().strftime("%d %B, %Y")
        #print(f"Form Passed\nStart : {session_start}\nEnd : {session_end}\nComment : {extra_comment}")
        save_data_to_csv([date,session_start, session_end, extra_comment])
    return render_template("add_ritual.html", form=form)

@app.route("/view_rituals")
def view_rituals():
    data = []
    try:
        with open(FILE_PATH, 'r') as file:
            data = csv.reader(file)
            all_rows = list(data)
            rituals = all_rows[1:]
        #print(f"rituals : {rituals}")
    except FileNotFoundError:
        print("File can't be found")
        rituals = []
    return render_template("view_rituals.html", rituals=rituals)

if __name__ == "__main__":
    app.run(debug=True)