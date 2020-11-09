from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Wall


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