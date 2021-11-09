#Learner Test lead by Ley Yi (refer to Learner Integration Test, Staff Test, Staff Integration Test, Trainer Test and Trainer Integration Test too)
import unittest
from unittest import mock
from unittest.mock import patch
import json
import os
from dbModel import *

def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == "backend-api/tdd_mockfiles/testLearner.json":
        return MockResponse({"message": "Successfully retrieved all learner"}, 200)

    return MockResponse(None, 404)

class test_Learner(unittest.TestCase):
    def setUp(self):
        self.learner= Learner(1, 0)

    def tearDown(self):
        self.learner = None

    def test_learner(self):
        learnerDetails = self.learner.json()
        self.assertEqual(learnerDetails, {
            "staffID": 1,
            "numberOfClassesPassed": 0}
        )

    def fetch_json(self, testfile):
        with open(testfile, "r") as myfile:
            response = json.load(myfile)
        data = response["data"]
        code = response["code"]

        return data, code


    @patch('requests.get', side_effect=mocked_requests_get)
    def test_get_all_learner(self, mock_get):
        if 'backend-api' not in os.getcwd():
            os.chdir("./backend-api")

        learner = test_Learner()
        try:
            json_data, code = learner.fetch_json("tdd_mockfiles/testLearner.json")
        except:
            json_data, code = learner.fetch_json("backend-api/tdd_mockfiles/testLearner.json")



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
        self.assertEqual(json_data, check_data)


if __name__ == "__main__":
    unittest.main()
