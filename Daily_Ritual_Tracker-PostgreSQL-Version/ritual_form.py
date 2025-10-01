from datetime import datetime
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf import FlaskForm

class RitualForm(FlaskForm):
    begin_time = StringField('Begin Time', validators=[DataRequired()], render_kw={"placeholder": "When the session start? (e.g., 8:00)"})
    finish_time = StringField('Finish Time', validators=[DataRequired()], render_kw={"placeholder": "When the session end? (e.g., 17:20)"})
    comment = TextAreaField('Additional comment', render_kw={"placeholder": "Enter any comment here ..."})
    submit = SubmitField('Submit')

    def validate_begin_time(self, begin_time):
        try:
            datetime.strptime(begin_time.data.strip(), '%H:%M')
        except ValueError:
            raise ValidationError('Invalid time format. Please use H:MM (e.g., 8:30)')
    def validate_finish_time(self, finish_time):
        try:
            datetime.strptime(finish_time.data.strip(), '%H:%M')
        except ValueError:
            raise ValidationError('Invalid time format. Please use H:MM (e.g., 17:00)')