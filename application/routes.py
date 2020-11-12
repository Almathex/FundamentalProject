from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Wall, Location, Activity
from application.forms import WallForm, OrderWall, ActivityForm

@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('index.html', title="WHERE IS THE WALL")

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = WallForm()
    if form.validate_on_submit():
        walls = Walls(
            wall = form.wall.data,
            complete = False
        )
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
     form = WallForm()
    return render_template('add.html', title="New Location", form=form)   
