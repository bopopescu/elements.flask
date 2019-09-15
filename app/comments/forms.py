from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired

class ForComment(FlaskForm):
	message = TextAreaField('Message', validators=[DataRequired()])
	submit = SubmitField('Send')