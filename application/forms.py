from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Walls, Locations, Activities

class LocationForm(FlaskForm):
    county = StringField('County:', validators = [DataRequired()])
    town = StringField('Town:', validators = [DataRequired()])
    postcode = StringField('Postcode:', validators = [DataRequired()])
    submit = SubmitField('Submit')

    def validate_task(self, task):
        locations = Locations.query.all()
        for location in locations:
            if location.postcode == postcode.data:
                raise ValidationError('This postcode already exists!')

class ActivityForm(FlaskForm):
    activity_name =  StringField('Activity:', validators = [DataRequired()])
    additional_equiptment = BooleanField('Equiptment required?:', validators = [DataRequired()])
    submit = SubmitField('Submit')

    def validate_task(self, task):
        activities = Activities.query.all()
        for activity in activities:
            if activity.activity_name == activity_name.data:
                raise ValidationError('This activity already exists!')
          
class OrderWall(FlaskForm):
    order_with = SelectField('Order With:',
        choices=[
            ("postcode", "Postcode"),
            ("id", "Newest"),
            ("old", "Oldest"),
            ('activity_name', "activity")
        ]
    )
    submit = SubmitField('Order by')          
