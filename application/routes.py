from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Walls, Locations, Activities
from application.forms import LocationForm, OrderWall, ActivityForm

@app.route('/', methods=['POST', 'GET'])
def index():
    form = OrderWall()
    totals = {
        "total_locations": Locations.query.count(),
        "total_activities": Activities.query.count()
    }
    return render_template('index.html', title="Wall App", form=form, totals=totals, locations=Locations.query.all(), activities=Activities.query.all())

@app.route('/add/location', methods=['POST', 'GET'])
def add():
    form = LocationForm()
    if form.validate_on_submit():
        location = Locations(
            wall_name = form.wall_name.data,
            county = form.county.data,
            town = form.town.data,
            postcode = form.postcode.data
        )
        db.session.add(location)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', title="New Wall", form=form) 

@app.route('/add/activity', methods=['POST', 'GET'])
def add1():
    form = ActivityForm()
    if form.validate_on_submit():
        activity = Activities(
            activity_name = form.activity_name.data,
            additional_equiptment = bool(form.additional_equiptment.data)
        )
        db.session.add(activity)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addact.html', title="New Activity", form=form)       

@app.route('/update/location/<int:id>', methods=['GET', 'POST'])
def updateloc(id):
    form = LocationForm()
    location = Locations.query.get(id)
    if form.validate_on_submit():
        location.county = form.county.data
        location.town = form.town.data
        location.postcode = form.postcode.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.county.data = location.county
        form.town.data = location.town
        form.postcode.data = location.postcode
    return render_template('update.html', title='Edit your location', form=form)


@app.route('/update/activity/<int:id>', methods=['GET', 'POST'])
def updateact(id):
    form = ActivityForm()
    activity = Activities.query.get(id)
    if form.validate_on_submit():
        activity.activity_name = form.activity_name.data
        activity.additional_equiptment = bool(form.additional_equiptment.data)
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.activity_name.data = activity.activity_name
        form.additional_equiptment.data = activity.additional_equiptment
    return render_template('updateact.html', title='Edit your activity', form=form)    

@app.route('/delete/location/<int:id>')
def deleteloc(id):
    location = Locations.query.get(id)
    db.session.delete(location)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/activity/<int:id>')
def deleteact(id):
    activity = Activities.query.get(id)
    db.session.delete(activity)
    db.session.commit()
    return redirect(url_for('index'))    