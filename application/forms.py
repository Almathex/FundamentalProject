from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Wall, Location, Activity


class WallForm(FlaskForm):
    wall = StringField('Wall name:', validators = [ DataRequired()])
    location = StringField('Location:', validators = [ DataRequired()])
    postcode = StringField('Postcode:', validators = [ DataRequired()])
    size = StringField('Size:', validators = [ DataRequired()])
    rating = IntegerField('Rating:', validators = [ DataRequired()])
    submit = SubmitField('Submit')

class ActivityForm(FlaskForm):
    activity = StringField('Activity:', validators = [DataRequired(),] )
    additional_equiptment = BooleanField('Need Equiptment:', validators = [ DataRequired()] )
    submit = SubmitField('Submit')

def validate_activity(self, activity):
    activities = Activity.query.all()
    for index in activities:
        if index.activity == activity.data:
            raise ValidationError('This activity already exists!')

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
