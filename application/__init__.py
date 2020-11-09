from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password1234@34.105.157.94/walls"
app.config['SECRET_KEY'] = "a-secret"

db = SQLAlchemy(app)

from application import routes
