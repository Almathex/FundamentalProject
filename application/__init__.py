from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['DBI_URI'] = getenv('DBI_URI')
app.config['SECRET_KEY'] = getenv('SECREY_KEY')
db = SQLAlchemy(app)

from application import routes
