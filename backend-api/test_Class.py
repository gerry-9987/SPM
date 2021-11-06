import unittest
from cclass import app, db
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

class ClassTestCase(TestingApp):

    def test_get_all_classes(self):
        class_endpoint = "/class"
        response = self.client().get(class_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
        check_data = {
                "classes": [
                    {
                        "classID": 1,
                        "classSize": 4,
                        "courseID": 1,
                        "endDate": "03 Feb 2021",
                        "endTime": "23:30:00",
                        "staffID": 3,
                        "startDate": "01 Jan 2021",
                        "startTime": "22:30:00",
                        "trainerName": "Haoyue"
                    },
                    {
                        "classID": 2,
                        "classSize": 4,
                        "courseID": 1,
                        "endDate": "03 Feb 2021",
                        "endTime": "01:30:00",
                        "staffID": 3,
                        "startDate": "01 Jan 2021",
                        "startTime": "12:30:00",
                        "trainerName": "Haoyue"
                    },
                    {
                        "classID": 3,
                        "classSize": 4,
                        "courseID": 2,
                        "endDate": "07 May 2021",
                        "endTime": "02:30:00",
                        "staffID": 3,
                        "startDate": "03 Feb 2021",
                        "startTime": "01:30:00",
                        "trainerName": "Haoyue"
                    },
                    {
                        "classID": 4,
                        "classSize": 4,
                        "courseID": 2,
                        "endDate": "07 May 2021",
                        "endTime": "03:30:00",
                        "staffID": 3,
                        "startDate": "03 Feb 2021",
                        "startTime": "02:30:00",
                        "trainerName": "Haoyue"
                    },
                    {
                        "classID": 5,
                        "classSize": 4,
                        "courseID": 2,
                        "endDate": "07 May 2021",
                        "endTime": "23:30:00",
                        "staffID": 4,
                        "startDate": "03 Feb 2021",
                        "startTime": "22:30:00",
                        "trainerName": "Jewel"
                    },
                    {
                        "classID": 6,
                        "classSize": 4,
                        "courseID": 2,
                        "endDate": "07 May 2021",
                        "endTime": "02:30:00",
                        "staffID": 4,
                        "startDate": "03 Feb 2021",
                        "startTime": "12:30:00",
                        "trainerName": "Jewel"
                    },
                    {
                        "classID": 7,
                        "classSize": 4,
                        "courseID": 3,
                        "endDate": "07 May 2021",
                        "endTime": "02:30:00",
                        "staffID": 4,
                        "startDate": "04 Mar 2021",
                        "startTime": "01:30:00",
                        "trainerName": "Jewel"
                    }
                    ]
        }
        self.assertEqual(code, 200)
        self.assertEqual(data, check_data)

    def test_get_specific_class(self):
        specific_class_endpoint = "/class/1"
        response = self.client().get(specific_class_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
        check_data = [
                        {
                        "classID": 1,
                        "classSize": 4,
                        "courseID": 1,
                        "endDate": "03 Feb 2021",
                        "endTime": "23:30:00",
                        "quizID": 1,
                        "staffID": 3,
                        "startDate": "01 Jan 2021",
                        "startTime": "22:30:00",
                        "trainerName": "Haoyue"
                        },
                        {
                        "classID": 2,
                        "classSize": 4,
                        "courseID": 1,
                        "endDate": "03 Feb 2021",
                        "endTime": "01:30:00",
                        "quizID": 2,
                        "staffID": 3,
                        "startDate": "01 Jan 2021",
                        "startTime": "12:30:00",
                        "trainerName": "Haoyue"
                        }
                    ]
        self.assertEqual(code, 200)
        self.assertEqual(data, check_data)
