#Staff Test lead by Ley Yi (refer to Staff Integration Test, Learner Test, Learner Integration Test, Trainer Test and Trainer Integration Test too)

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

    if args[0] == "backend-api/tdd_mockfiles/testStaff.json":
        return MockResponse({"message": "Successfully retrieved all staff"}, 200)

    return MockResponse(None, 404)
class test_Staff(unittest.TestCase):
    def setUp(self):
        self.staff= Staff(1, 'alice231', 'Alice Woo', 'trainer')

    def tearDown(self):
        self.staff = None

    def test_staff(self):
        staffDetails = self.staff.json()
        self.assertEqual(staffDetails, {
            "staffID": 1,
            "staffUsername": 'alice231',
            "staffName": 'Alice Woo',
            "department": 'trainer'}
        )

    def fetch_json(self, testfile):
        with open(testfile, "r") as myfile:
            response = json.load(myfile)
        data = response["data"]
        code = response["code"]

        return data, code


    @patch('requests.get', side_effect=mocked_requests_get)
    def test_get_all_staff(self, mock_get):
        if 'backend-api' not in os.getcwd():
            os.chdir("./backend-api")

        staff = test_Staff()
        try:
            json_data, code = staff.fetch_json("tdd_mockfiles/testStaff.json")
        except:
            json_data, code = staff.fetch_json("backend-api/tdd_mockfiles/testStaff.json")



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
        self.assertEqual(json_data, check_data)


if __name__ == "__main__":
    unittest.main()
