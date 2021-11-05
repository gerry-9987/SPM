import unittest
from unittest import mock
import requests

from dbModel import *

def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == "test/testChapters.json":
        return MockResponse({"message": "Success retrieval"}, 200)
    elif args[0] == "test/testChapter.json":
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

    def fetch_json(self, url):
        response = requests.get(url)
        data = response.data
        code = response.code
        return data.json(), code

    
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_all_chapters(self, mock_get):
        mychapter = test_Chapter()
        json_data, code = mychapter.fetch_json("test/testChapters.json")
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

if __name__ == "__main__":
    unittest.main()
