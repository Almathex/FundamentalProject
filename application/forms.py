from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Walls, Locations, Activities

class LocationForm(FlaskForm):
    wall_name = StringField('Wall name:', validators = [DataRequired()])
    county = StringField('County:', validators = [DataRequired()])
    town = StringField('Town:', validators = [DataRequired()])
    postcode = StringField('Postcode:', validators = [DataRequired()])
    submit = SubmitField('Submit')



class ActivityForm(FlaskForm):
    activity_name =  StringField('Activity:', validators = [DataRequired()])
    additional_equiptment = SelectField('Order With:',
        choices=[
            ("True", "Yes"),
            ("", "No")]
    )
    submit = SubmitField('Submit')

          
class OrderWall(FlaskForm):
    order_with = SelectField('Order With:',
        choices=[
            ("wall_name", "Name"),
            ("id", "Most Recent"),
            ("old", "Oldest"),
            ('activity_name', "activity")
        ]
    )
    submit = SubmitField('Order by')          
