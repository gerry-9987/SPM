#Staff Integration Test lead by Ley Yi (refer to Staff Test, Learner Test, Learner Integration Test, Trainer Test and Trainer Integration Test too)

import unittest
from staff import app, db

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

    def test_get_all_staff(self):
        staff_endpoint = "/staff"
        response = self.client().get(staff_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
        check_data = {
            "staff": [
                    {
                        "department": "Learner", 
                        "staffID": 1, 
                        "staffName": "Geraldine", 
                        "staffUsername": "gerry"
                    }, 
                    {
                        "department": "Learner", 
                        "staffID": 2, 
                        "staffName": "Ley Yi", 
                        "staffUsername": "ly"
                    }, 
                    {
                        "department": "Trainer", 
                        "staffID": 3, 
                        "staffName": "Haoyue", 
                        "staffUsername": "gellybear"
                    }, 
                    {
                        "department": "Trainer", 
                        "staffID": 4, 
                        "staffName": "Jewel", 
                        "staffUsername": "jewel"
                    }, 
                    {
                        "department": "Administrator", 
                        "staffID": 5, 
                        "staffName": "Wesley", 
                        "staffUsername": "wesley"
                    }, 
                    {
                        "department": "Learner", 
                        "staffID": 6, 
                        "staffName": "AAAAA", 
                        "staffUsername": "AAA"
                    }, 
                    {
                        "department": "Learner", 
                        "staffID": 7, 
                        "staffName": "BBBBB", 
                        "staffUsername": "BBB"
                    }, 
                    {
                        "department": "Learner", 
                        "staffID": 8, 
                        "staffName": "CCCCCC", 
                        "staffUsername": "CCC"
                    }, 
                    {
                        "department": "Learner", 
                        "staffID": 9, 
                        "staffName": "DDDDDDD", 
                        "staffUsername": "DDD"
                    }, 
                    {
                        "department": "Administrator", 
                        "staffID": 10, 
                        "staffName": "EEEEEE", 
                        "staffUsername": "EEE"
                    }
                ]
        }
        self.assertEqual(code, 200)
        self.assertEqual(data, check_data)
    def test_get_staff(self):
        staff_endpoint = "/staff/1"
        response = self.client().get(staff_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
        check_data = {
            "department": "Learner", 
            "staffID": 1, 
            "staffName": "Geraldine", 
            "staffUsername": "gerry"
        }
        self.assertEqual(code, 200)
        self.assertEqual(data, check_data)
