from flask import Blueprint
from flask import render_template
from .forms import ForComment
from flask import request 
from flask import url_for
from flask import redirect

from models import Comments
from app import db

from flask_security import login_required

comments = Blueprint('comments', __name__, template_folder='templates')

@comments.route('/', methods=['GET', 'POST'])	
@login_required
def vcomments():
	form = ForComment()
	if request.method == 'POST':
		message = request.form['message']
		try:
			mes = Comments(comment=message)
			db.session.add(mes)
			db.session.commit()
		except:
			print('Please try again')
		return redirect(url_for('comments.vcomments'))
	comm = Comments.query.order_by(Comments.created.desc())
	page = request.args.get('page')
	if page and page.isdigit():
		page = int(page)
	else:
		page = 1
	pages = comm.paginate(page=page,per_page=3)
	return render_template('comments/comments.html', form=form, comm=pages)
