import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Locations, Activities

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlitte:///data.db",
        SECRET_KEY='TEST_SECRET_KEY',
        DEBUG=True)
        return app

    def setUp(self):
        db.create_all()
        location = Locations(wall_name='The big one', county='Cheshire', town='Chester', postcode='CH1 4HX')
        activity1 = Activities(wall_id=1, activity_name='Rock Climbing', additional_equiptment=1)
        db.activities.add(location)
        db.activities.add(activity1)
        db.activities.commit()

    def tearDown(self):
        db.activities.remove()
        db.drop_all()
