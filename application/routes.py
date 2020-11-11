from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Wall, Location, Activity
from application.forms import WallForm, OrderWall, LocationForm, ActivityForm

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', title="WHERE IS THE WALL")

@app.route('/add', methods=['POST', 'GET'])
def add():
    return render_template('add.html', title="New Location")   
