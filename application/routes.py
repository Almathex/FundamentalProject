from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Wall, Location, Activity
from application.forms import WallForm, LocationForm, ActivityForm

@app.route('/', methods=['POST', 'GET'])
def index():
    form = OrderWall()
    totals = {
        "total_walls": Wall.query.count(),
        "total_locations": Location.query.count(),
        "total_activites": Activity.query.count()
    }
    if form.order_with.data == "id":
        wall = Wall.query.order_by(Wall.id.desc()).all()
    elif form.order_with.data == "location":
        wall = Wall.query.order_by(Wall.location_id.desc()).all()
    elif form.order_with.data == "activity":
        wall = Wall.query.order_by(Wall.activity_id).all()
    else:
        wall = Wall.query.all()
    return render_template('index.html', title="WallFinder App", wall=wall, form=form, totals=totals)

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = LocationForm()
    if form.validate_on_submit():
        location = Location(
            locations = form.location.data,
        )
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', title="New Location", form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = WallForm()
    wall = Wall.query.get(id)
    if form.validate_on_submit():
        wall.walls = form.walls.data
        db.session.commit()
        redirect(url_for('index'))
    elif request.method == 'GET':
        form.walls.data = wall.walls
    return render_template('update.html', title='Edit your wall', form=form)    
