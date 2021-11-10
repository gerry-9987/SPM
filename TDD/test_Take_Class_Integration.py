# Class Take_Class Integration Test led by Tey Haoyue (refer to Class Unit Test, Take_Class Unit Test too)
import unittest
from takeClass import app, db
from textwrap import wrap

import json
from ast import literal_eval

class TestingApp(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        self.maxDiff = None
        with self.app.app_context():
            db.create_all()
        self.assertIsNotNone(self.app, "Failed to load app")
        self.assertIsNotNone(self.client, "Failed to load client")

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TakeClassTestCase(TestingApp):

    def test_get_all_classes(self):
        take_class_endpoint = "/take_class"
        response = self.client().get(take_class_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
        check_data = {
            "classes_taken": [
            {
                "classID": 1,
                "courseID": 1,
                "courseName": "IBM 101",
                "staffID": 1
            },
            {
                "classID": 7,
                "courseID": 3,
                "courseName": "HP 101",
                "staffID": 1
            },
            {
                "classID": 2,
                "courseID": 1,
                "courseName": "IBM 102",
                "staffID": 2
            },
            {
                "classID": 3,
                "courseID": 2,
                "courseName": "HP 101",
                "staffID": 6
            },
            {
                "classID": 4,
                "courseID": 2,
                "courseName": "HP 102",
                "staffID": 7
            },
            {
                "classID": 5,
                "courseID": 2,
                "courseName": "Xerox 101",
                "staffID": 8
            },
            {
                "classID": 6,
                "courseID": 2,
                "courseName": "Xerox 102",
                "staffID": 9
            }
    ]
        }
        self.assertEqual(code, 200)
        self.assertEqual(data, check_data)

    def test_get_specific_class_taken(self):
        specific_class_taken_endpoint = "/take_class/1"
        response = self.client().get(specific_class_taken_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
        check_data =  {
            "classID": 1,
            "courseID": 1,
            "courseName": "IBM 101",
            "staffID": 1
        }
        self.assertEqual(code, 200)
        self.assertEqual(data, check_data)
