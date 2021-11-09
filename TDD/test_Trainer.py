#Trainer Test lead by Ley Yi (refer to Trainer Integration Test, Staff Test, Staff Integration Test, Learner Test and Learner Integration Test too)

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

    if args[0] == "TDD/tdd_mockfiles/testTrainer.json":
        return MockResponse({"message": "Successfully retrieved all trainer"}, 200)

    return MockResponse(None, 404)

class test_Trainer(unittest.TestCase):
    def setUp(self):
        self.trainer= Trainer(3, 1)

    def tearDown(self):
        self.trainer = None

    def test_trainer(self):
        trainerDetails = self.trainer.json()
        self.assertEqual(trainerDetails, {
            "staffID": 3,
            "numberOfClasses": 1,
            }
        )
    
    def fetch_json(self, testfile):
        with open(testfile, "r") as myfile:
            response = json.load(myfile)
        data = response["data"]
        code = response["code"]

        return data, code


    @patch('requests.get', side_effect=mocked_requests_get)
    def test_get_all_trainer(self, mock_get):
        if 'TDD' not in os.getcwd():
            os.chdir("./TDD")

        trainer = test_Trainer()
        try:
            json_data, code = trainer.fetch_json("tdd_mockfiles/testTrainer.json")
        except:
            json_data, code = trainer.fetch_json("TDD/tdd_mockfiles/testTrainer.json")



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
        self.assertEqual(json_data, check_data)


if __name__ == "__main__":
    unittest.main()
