import unittest
from unittest import mock
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

    if args[0] == "backend-api/tdd_mockfiles/testMaterials.json":
        return MockResponse({"message": "Successfully retrieved all materials"}, 200)
    elif args[0] == "backend-api/tdd_mockfiles/testMaterial.json":
        return MockResponse({"message": "Successfully retrieved material based on chapterID"}, 200)

    return MockResponse(None, 404)

class test_Material(unittest.TestCase):
    def setUp(self):
        self.material = Material(2, 'Google', 'link', 'www.google.com', 'Google website to search for anything', 2, 1, 1)

    def tearDown(self):
        self.chapter = None

    def test_material_details(self):
        materialDetails = self.material.json()
        checkMaterial = {
            "materialID": 2,
            "materialName": 'Google',
            "materialType": 'link',
            "materialLink": 'www.google.com',
            "materialLinkBody": 'Google website to search for anything',
            "chapterID": 2,
            "classID": 1,
            "courseID": 1
            }
        self.assertEqual(materialDetails, checkMaterial)

    def fetch_json(self, testfile):
        with open(testfile, "r") as myfile:
            response = json.load(myfile)
        data = response["data"]
        code = response["code"]

        return data, code


    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_all_materials(self, mock_get):
        mymaterial = test_Material()
        json_data, code = mymaterial.fetch_json("backend-api/tdd_mockfiles/testMaterials.json")
        check_data = {
            "material": [
                {
                    "chapterID": 1,
                    "classID": 1,
                    "courseID": 1,
                    "materialID": 1,
                    "materialLink": "https://cseweb.ucsd.edu/classes/sp15/cse190-c/reports/sp15/048.pdf",
                    "materialLinkBody": "Predicting if income exceeds $50,000 per year based on 1994 US Census Data with\nSimple Classification Techniques",
                    "materialName": "Census Income",
                    "materialType": "document"
                },
                {
                    "chapterID": 2,
                    "classID": 1,
                    "courseID": 1,
                    "materialID": 2,
                    "materialLink": "https://www.google.com/",
                    "materialLinkBody": "You can learn more about google",
                    "materialName": "About google",
                    "materialType": "link"
                }
            ]
        }
        self.assertEqual(code, 200)
        self.assertEqual(json_data, check_data)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_specific_material(self, mock_get):
        mymaterial = test_Material()
        json_data, code = mymaterial.fetch_json("backend-api/tdd_mockfiles/testMaterial.json")
        check_data = [
            {
                "chapterID": 1,
                "classID": 1,
                "courseID": 1,
                "materialID": 1,
                "materialLink": "https://cseweb.ucsd.edu/classes/sp15/cse190-c/reports/sp15/048.pdf",
                "materialLinkBody": "Predicting if income exceeds $50,000 per year based on 1994 US Census Data with\nSimple Classification Techniques",
                "materialName": "Census Income",
                "materialType": "document"
            }
        ]
        self.assertEqual(code, 200)
        self.assertEqual(json_data, check_data)



if __name__ == "__main__":
    unittest.main()
