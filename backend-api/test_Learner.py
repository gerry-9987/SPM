# import unittest
# from dbModel import *

# class test_Learner(unittest.TestCase):
#     def setUp(self):
#         self.learner= Learner(1, 0)

#     def tearDown(self):
#         self.learner = None

#     def test_staff(self):
#         learnerDetails = self.learner.json()
#         self.assertEqual(learnerDetails, {
#             "staffID": 1,
#             "numberOfClassesPassed": 0}
#         )
import unittest
from learner import app, db

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

    def test_get_all_learner(self):
        learner_endpoint = "/learner"
        response = self.client().get(learner_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
        check_data = {
            "learners": [
                {
                    "numberOfClassesPassed": 1, 
                    "staffID": 1
                }, 
                {
                    "numberOfClassesPassed": 1, 
                    "staffID": 2
                }, 
                {
                    "numberOfClassesPassed": 1, 
                    "staffID": 6
                }, 
                {
                    "numberOfClassesPassed": 1, 
                    "staffID": 7
                }, 
                {
                    "numberOfClassesPassed": 1, 
                    "staffID": 8
                }, 
                {
                    "numberOfClassesPassed": 1, 
                    "staffID": 9
                }
            ]
        }
        self.assertEqual(code, 200)
        self.assertEqual(data, check_data)
    def test_get_learner(self):
        learner_endpoint = "/learner/1"
        response = self.client().get(learner_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
        check_data = {
            "numberOfClassesPassed": 1, 
            "staffID": 1
        }
        self.assertEqual(code, 200)
        self.assertEqual(data, check_data)