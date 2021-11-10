# Class class Unit Test led by Tey Haoyue (refer to Class class Integration Test, Class Take_Class Integration Test, Take_Class class Unit Test too)
import requests
import unittest
from unittest import mock
from unittest.mock import patch
import json
import os
from dbModel import *

# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'TDD/tdd_mockfiles/testClasses.json':
        return MockResponse({"message": "All classes have been retrieved!"}, 200)
    elif args[0] == 'TDD/tdd_mockfiles/testClass.json':
        return MockResponse({"message": "A specific class has been retrieved!"}, 200)

    return MockResponse({"Message": "There are no classes."}, 404)


class test_Class(unittest.TestCase):
    def setUp(self):
        self.aclass = Class(1, 1, '01 Jan 2021', '03 Feb 2021', '22:30:00', '23:30:00', 4, 'Haoyue', 3, 1)

    def tearDown(self):
        self.aclass = None

    def test_class_details(self):
        classDetails = self.aclass.json()
        checkClass = {
            "classID": 1,
            "courseID": 1,
            "startDate": '01 Jan 2021',
            "endDate": '03 Feb 2021',
            "startTime": '22:30:00',
            "endTime": '23:30:00',
            "classSize": 4,
            "trainerName": 'Haoyue',
            "staffID": 3,
            "quizID": 1
            }
        self.assertEqual(classDetails, checkClass)

    def fetch_json(self, testfile):
        with open(testfile, "r") as myfile:
            response = json.load(myfile)
        data = response["data"]
        code = response["code"]

        return data, code

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_class(self, mock_get):

        if 'TDD' not in os.getcwd():
            os.chdir("./TDD")

        aclass = test_Class()

        try:
            json_data, code = aclass.fetch_json('tdd_mockfiles/testClass.json')
        except:
            json_data, code = aclass.fetch_json('TDD/tdd_mockfiles/testClass.json')

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
                }
            ]
        }

        self.assertEqual(code, 200)
        self.assertEqual(json_data, check_data)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_get_classes(self, mock_get):

        if 'TDD' not in os.getcwd():
            os.chdir("./TDD")

        aclass = test_Class()
        
        try:
            json_data, code = aclass.fetch_json('tdd_mockfiles/testClasses.json')
        except:
            json_data, code = aclass.fetch_json('TDD/tdd_mockfiles/testClasses.json')

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
                }
            ]
        }
        self.assertEqual(code, 200)
        self.assertEqual(json_data, check_data)


