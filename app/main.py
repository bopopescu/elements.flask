from app import app
from app import db

from comments.blueprint import comments
from feedback.blueprint import feedback
from view import *

app.register_blueprint(comments, url_prefix='/comments')
app.register_blueprint(feedback, url_prefix='/feedback')


if __name__ == '__main__':
	app.run()