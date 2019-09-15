from app import app
from flask import render_template
from forms import Registration
from flask import redirect
from app import user_datastore
from app import db
from flask import request
from flask import url_for
from models import Role

from flask_login import logout_user

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
	if request.method == 'POST':
		try:
			user = user_datastore.create_user(email=request.form['email'], password=request.form['password'])
			role=Role.query[1]
			user_datastore.add_role_to_user(user,role)
			db.session.commit()
		except:
			print('Please try again.')
		return redirect(url_for('security.login'))
	form = Registration()
	return render_template('security/register.html', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index.html'))




