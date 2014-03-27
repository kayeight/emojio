from flask import Flask
from settings import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{0}:{1}@{2}/{3}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

from models import db
db.init_app(app)

import emoji.routes