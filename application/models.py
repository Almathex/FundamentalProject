from application import db

class Wall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'), nullable =False)
    nickname = db.Column(db.String(30), unique=True)
    wall_size = db.Column(db.String(30), unique=True)
    ease_of_acces = db.Column(db.Integer(10))
    rating = db.Column(db.Float(5), nullable=True)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    county = db.Column(db.String(50), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)
    loctaions = db.realationship('Wall', backref = 'location')
    
class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_name =  db.Column(db.String(50), unique=True)
    Additional_equiptment = db.Column(db.Boolean, nullable=False)
    activities = db.realationship('Wall', backref = 'activity')
