from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Wall, Location, Activity


class WallForm(FlaskForm):
    wall = StringField('Wall:',
        validators = [
            DataRequired(),
        ]    
    )
    submit = SubmitField('Submit')

    def validate_task(self, wall):
        walls = Wall.query.all()
        for index in walls:
            if index.wall == wall.data:
                raise ValidationError('This wall already exists!')

class LocationForm(FlaskForm):
    location = StringField('Location:',
        validators = [
            DataRequired(),
        ]    
    )
    submit = SubmitField('Submit')

    def validate_task(self, location):
        locations = Location.query.all()
        for index in locations:
            if index.location == location.data:
                raise ValidationError('This wall already exists!')            


class ActivityForm(FlaskForm):
    activity = StringField('Activity:',
        validators = [
            DataRequired(),
        ]    
    )
    submit = SubmitField('Submit')

    def validate_task(self, activity):
        activities = Activity.query.all()
        for index in activities:
            if index.activity == activity.data:
                raise ValidationError('This wall already exists!')

class OrderWall(FlaskForm):
    order_with = SelectField('Order With:',
        choices=[
            ("location", "Location"),
            ("id", "Newest"),
            ("old", "Oldest"),
            ('activity', "Activity")
        ]
    )
    submit = SubmitField('Confirm')            