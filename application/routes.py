from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Wall, Location, Activity
from application.forms import WallForm, OrderWall, ActivityForm

@app.route('/', methods=['POST', 'GET'])
def index():
    wall = Wall()
    return render_template('index.html', title="WHERE IS THE WALL", wall=wall)

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = WallForm()
    if form.validate_on_submit():
        walls = Walls(
            wall = form.wall.data,
            complete = False
        )
        db.session.add(walls)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', title="New Location", form=form)   

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = WallForm()
    wall = Walls.query.get(id)
    if form.validate_on_submit():
        wall.size = form.size.data
        db.session.commit()
        redirect(url_for('index'))
    elif request.method == 'GET':
        form.size.data = wall.size
    return render_template('update.html', title='Update your wall', form=form)

@app.route('/delete/<int:id>')
def delete(id):
    wall = Walls.query.get(id)
    db.session.delete(wall)
    db.session.commit()
    return redirect(url_for('index'))