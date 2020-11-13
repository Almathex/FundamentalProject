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
    return render_template('index.html', title="Wall App", form=form, totals=totals, locations=Locations.query.all())

@app.route('/add/location', methods=['POST', 'GET'])
def add():
    form = LocationForm()
    if form.validate_on_submit():
        location = Locations(
            wall_name = form.wall_name.data,
            county = form.county.data,
            town = form.town.data,
            postcode = form.postcode.data )
        db.session.add(location)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addwall.html', title="New Wall", form=form) 

@app.route('/add/activity/<idnum>', methods=['POST', 'GET'])
def add1(idnum):
    form = ActivityForm()
    if form.validate_on_submit():
        activity = Activities(
        wall_id = idnum,
        activity_name = form.activity_name.data,
        additional_equiptment = bool(form.additional_equiptment.data)
        )
        db.session.add(activity)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addactivity.html', title="New Activity", form=form, locations=Locations.query.get(idnum))       

@app.route('/update/location/<idnum>', methods=['GET', 'POST'])
def updateloc(idnum):
    form = LocationForm()
    location = Locations.query.get(idnum)
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
    return render_template('updatewall.html', title='Edit your wall', form=form)


@app.route('/update/activity/<idnum>', methods=['GET', 'POST'])
def updateact(idnum):
    form = ActivityForm()
    activity = Activities.query.get(idnum)
    if form.validate_on_submit():
        activity.activity_name = form.activity_name.data
        activity.additional_equiptment = bool(form.additional_equiptment.data)
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.activity_name.data = activity.activity_name
        form.additional_equiptment.data = activity.additional_equiptment
    return render_template('updateactivity.html', title='Edit your activity', form=form)    

@app.route('/view/<idnum>', methods=['POST', 'GET'])
def viewactivity(idnum):

    return render_template('viewactivity.html', activities = Activities.query.filter_by(wall_id=idnum).all(), locations = Locations.query.get(idnum))    

@app.route('/delete/location/<idnum>')
def deleteloc(idnum):
    location = Locations.query.get(idnum)
    db.session.delete(location)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/activity/<idnum>')
def deleteact(idnum):
    activity = Activities.query.get(idnum)
    db.session.delete(activity)
    db.session.commit()
    return redirect(url_for('index'))    