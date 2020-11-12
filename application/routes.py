from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Walls, Locations, Activities
from application.forms import LocationForm, OrderWall, ActivityForm

@app.route('/', methods=['POST', 'GET'])
def index():
    form = OrderWall()
    totals = {
        "total locations": Locations.query.count(),
        "total_activities": Activities.query.count()
    }
    return render_template('index.html', title="Wall App", form=form, totals=totals)

@app.route('/add/location', methods=['POST', 'GET'])
def add():
    form = LocationForm()
    if form.validate_on_submit():
        location = Locations(
            county = form.county.data,
            town = form.town.data,
            postcode = form.town.data
        )
        db.session.add(location)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', title="New Location", form=form)    

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = LocationForm()
    location = Locations.query.get(id)
    if form.validate_on_submit():
        location.county = form.county.data
        location.town = form.town.data
        location.postcode = form.postcode.data
        db.session.commit()
        redirect(url_for('index'))
    elif request.method == 'GET':
        form.county.data = location.county
        form.town.data = location.town
        form.postcode.data = location.postcode
    return render_template('update.html', title='Edit your location', form=form)

@app.route('/delete/<int:id>')
def delete(id):
    location = Locations.query.get(id)
    db.session.delete(location)
    db.session.commit()
    return redirect(url_for('index'))