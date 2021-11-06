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

    if args[0] == "tdd_mockfiles/testChapters.json":
        return MockResponse({"message": "Successfully retrieved all chapters"}, 200)
    elif args[0] == "tdd_mockfiles/testChapter.json":
        return MockResponse({"message": "Successfully retrieved based on chapterID"}, 200)

    return MockResponse(None, 404)

class test_Chapter(unittest.TestCase):
    def setUp(self):
        self.chapter = Chapter(7, "Week 7 TDD", "Learn about test-driven development", 5)

    def tearDown(self):
        self.chapter = None

    def test_chapter_details(self):
        chapterDetails = self.chapter.json()
        print(chapterDetails)
        checkChapter = {
            "chapterID": 7,
            "chapterName": 'Week 7 TDD',
            "chapterDetails": 'Learn about test-driven development',
            "quizID": 5
            }
        self.assertEqual(chapterDetails, checkChapter)

    def fetch_json(self, testfile):
        with open(testfile, "r") as myfile:
            response = json.load(myfile)
        data = response["data"]
        code = response["code"]
        return data, code


    @patch('requests.get', side_effect=mocked_requests_get)
    def test_get_all_chapters(self, mock_get):
        if 'backend-api' not in os.getcwd():
            os.chdir("./backend-api")
        mychapter = test_Chapter()
        try:
            json_data, code = mychapter.fetch_json("tdd_mockfiles/testChapters.json")
        except:
            json_data, code = mychapter.fetch_json("backend-api/tdd_mockfiles/testChapters.json")

        check_data = [
                {
                    "chapterID": 1,
                    "chaperName": "Happy",
                    "chapterDetails": "Be Happy",
                    "quizID": 1
                },
                {
                    "chapterID": 2,
                    "chaperName": "Anger",
                    "chapterDetails": "Manage your anger",
                    "quizID": 3
                }
            ]
        self.assertEqual(code, 200)
        self.assertEqual(json_data, check_data)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_get_specific_chapter(self, mock_get):
        if 'backend-api' not in os.getcwd():
            os.chdir("./backend-api")

        mychapter = test_Chapter()
        try:
            json_data, code = mychapter.fetch_json("tdd_mockfiles/testChapter.json")
        except:
            json_data, code = mychapter.fetch_json("backend-api/tdd_mockfiles/testChapter.json")
        check_data = {
            "chapterDetails": "A cat is running away",
            "chapterID": 1,
            "chapterName": "CAT",
            "quizID": 1
        }
        self.assertEqual(code, 200)
        self.assertEqual(json_data, check_data)



if __name__ == "__main__":
    unittest.main()
