from flask import Blueprint
from flask import render_template

from flask import request
from flask import redirect
from flask import url_for

from flask_mail import Message 

from .forms import ForFeedback
from app import mail
from flask_mail import Mail

feedback = Blueprint('feedback', __name__, template_folder='templates')

@feedback.route('/', methods=['GET', 'POST'])
def vfeedback():
	feedback = ForFeedback()
	if request.method == 'POST':
		mes = request.form['message']
		try:
			msg = Message('Post', sender="logopedlee.ru@gmail.com", recipients=["denislee98@gmail.com"])
			msg.body = mes
			mail.send(msg)
		except:
			print("Please try again.")
		redirect(url_for('index'))
	return render_template('feedback/feedback.html', feedback=feedback)