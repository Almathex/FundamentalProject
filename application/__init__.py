from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
app = Flask(__name__)

app.config['DBI_URI'] = getenv('DBI_URI')
app.config['SECRET_KEY'] = 'a-secret-key'
db = SQLAlchemy(app)

from application import routes
