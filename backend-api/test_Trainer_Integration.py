import unittest
from trainer import app, db

import json
from ast import literal_eval

class TestingApp(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class StaffTestCase(TestingApp):

    def test_get_all_trainer(self):
        trainer_endpoint = "/trainer"
        response = self.client().get(trainer_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
        check_data = {
            "trainers": [
                {
                    "numberOfClasses": 10, 
                    "staffID": 3
                }, 
                {
                    "numberOfClasses": 8, 
                    "staffID": 4
                }
                ]
        }
        self.assertEqual(code, 200)
        self.assertEqual(data, check_data)
    def test_get_trainer(self):
        learner_endpoint = "/trainer/3"
        response = self.client().get(learner_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
        check_data = {
            "numberOfClasses": 10, 
            "staffID": 3
        }
        self.assertEqual(code, 200)
        self.assertEqual(data, check_data)