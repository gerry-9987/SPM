# Take_Class class Unit Test led by Tey Haoyue (refer to Class class Integration Test, Class class Unit Test too)
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

    if args[0] == 'TDD/tdd_mockfiles/testTake_Classes.json':
        return MockResponse({"message": "All classes taken have been retrieved!"}, 200)
    elif args[0] == 'TDD/tdd_mockfiles/testTake_Class.json':
        return MockResponse({"message": "A specific class taken has been retrieved!"}, 200)

    return MockResponse({"Message": "There are no classes taken."}, 404)


class test_Take_Class(unittest.TestCase):
    def setUp(self):
        self.aclasstaken = Take_Class(1, 1, 'IBM 101', 1)

    def tearDown(self):
        self.aclasstaken = None

    def test_class_details(self):
        classTakenDetails = self.aclasstaken.json()
        checkClassTaken = {
            "staffID": 1,
            "courseID": 1,
            "courseName": 'IBM 101',
            "classID": 1,          
            }
        self.assertEqual(classTakenDetails, checkClassTaken)

    def fetch_json(self, testfile):
        with open(testfile, "r") as myfile:
            response = json.load(myfile)
        data = response["data"]
        code = response["code"]

        return data, code

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_class_taken(self, mock_get):

        if 'TDD' not in os.getcwd():
            os.chdir("./TDD")

        aclasstaken = test_Take_Class()

        try:
            json_data, code = aclasstaken.fetch_json('tdd_mockfiles/testTake_Class.json')
        except:
            json_data, code = aclasstaken.fetch_json('TDD/tdd_mockfiles/testTake_Class.json')

        check_data = {
            "classes_taken": [
                {
                    "classID": 1,
                    "courseID": 1,
                    "courseName": "IBM 101",
                    "staffID": 1
                }
            ]
        }

        self.assertEqual(code, 200)
        self.assertEqual(json_data, check_data)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_get_classes_taken(self, mock_get):

        if 'TDD' not in os.getcwd():
            os.chdir("./TDD")

        aclasstaken = test_Take_Class()
        
        try:
            json_data, code = aclasstaken.fetch_json('tdd_mockfiles/testTake_Classes.json')
        except:
            json_data, code = aclasstaken.fetch_json('TDD/tdd_mockfiles/testTake_Classes.json')

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
                }

            ]
        }
        self.assertEqual(code, 200)
        self.assertEqual(json_data, check_data)


