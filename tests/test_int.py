import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Locations, Activities


class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        app.config['SECRET_KEY'] = 'supercalafragalistic'
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/smithalexanderbradley/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestAdd(TestBase):

    def test_add(self):
        """
        Test that a user can add a game if all the field are correctly filled out
        """

        # Click register menu link
        self.driver.find_element_by_xpath("/html/body/a[2]").click()
        time.sleep(1)
        test_wall_name='The big one'
        test_county='Cheshire'
        test_town='Chester'
        test_postcode='CH1 2AB'
        
        # Fill in registration form
        self.driver.find_element_by_xpath('//*[@id="wall"]').send_keys(test_wall_name)
        self.driver.find_element_by_xpath('//*[@id="county"]').send_keys(
            test_county)
        self.driver.find_element_by_xpath('//*[@id="town"]').send_keys(
            test_town)
        self.driver.find_element_by_xpath('//*[@id="postcode"]').send_keys(
            test_postcode)        
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)
        

        # Assert that browser redirects to index page
        assert url_for('index') in self.driver.current_url

if __name__ == '__main__':
    unittest.main(port=5000)