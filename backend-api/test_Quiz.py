#Quiz Class Unit Test lead by Geraldine (refer to Quiz Integration Test too)

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

    if args[0] == "backend-api/tdd_mockfiles/testQuiz.json":
        return MockResponse({"message": "Successfully retrieved all quizzes"}, 200)


    return MockResponse(None, 404)


class test_Quiz(unittest.TestCase):
    def setUp(self):
        self.quiz = Quiz(7, '01 Jan 2021', '03 Jan 2021', 'Is cat cute?', 'True', 20, 5)

    def tearDown(self):
        self.quiz = None

    def test_quiz_details(self):
        quizDetails = self.quiz.json()
        self.assertEqual(quizDetails, {
            "quizID": 7,
            "startDate": '01 Jan 2021',
            "endDate": '03 Jan 2021',
            "questions": 'Is cat cute?',
            "answers": 'True',
            "duration": 20,
            "passingScore": 5
            
            }
        )
    def fetch_json(self, testfile):
        with open(testfile, "r") as myfile:
            response = json.load(myfile)
        data = response["data"]
        code = response["code"]

        return data, code


    @patch('requests.get', side_effect=mocked_requests_get)
    def test_get_all_quizzes(self, mock_get):
        if 'backend-api' not in os.getcwd():
            os.chdir("./backend-api")

        myquiz = test_Quiz()
        try:
            json_data, code = myquiz.fetch_json("tdd_mockfiles/testQuiz.json")
        except:
            json_data, code = myquiz.fetch_json("backend-api/tdd_mockfiles/testQuiz.json")



        check_data = {
            "quiz": [
                {
                    "answers": "True, True, True, True, False, True, False, True",
                    "duration": 100,
                    "endDate": "03 Jan 2021",
                    "passingScore": 50,
                    "questions": "Is cat cute?, Is dog cute?, Does SPM teach pair programming?, Do chickens lay eggs?, Can chickens swim?, Can monkeys dance?, Can birds talk?, Is this module fun?",
                    "quizID": 1,
                    "startDate": "01 Jan 2021"
                },
                {
                    "answers": "True, True, True, True, False",
                    "duration": 60,
                    "endDate": "03 Jan 2021",
                    "passingScore": 35,
                    "questions": "Is dog cute?, Is catdog cute?, Does SPM teach pair programming?, Do chickens lay eggs, Can chickens swim?",
                    "quizID": 2,
                    "startDate": "01 Jan 2021"
                },
                {
                    "answers": "True, False, True, False",
                    "duration": 30,
                    "endDate": "03 Jan 2021",
                    "passingScore": 25,
                    "questions": "Can monkeys dance?, Can birds talk?, Is this module fun?, Is life cute?, ",
                    "quizID": 3,
                    "startDate": "01 Jan 2021"
                },
                {
                    "answers": "False",
                    "duration": 10,
                    "endDate": "03 Jan 2021",
                    "passingScore": 0,
                    "questions": "Is foetus cute?",
                    "quizID": 4,
                    "startDate": "01 Jan 2021"
                },
                {
                    "answers": "True",
                    "duration": 10,
                    "endDate": "07 Feb 2021",
                    "passingScore": 0,
                    "questions": "Is baby cute?",
                    "quizID": 5,
                    "startDate": "03 Jan 2021"
                },
                {
                    "answers": "True",
                    "duration": 10,
                    "endDate": "07 Feb 2021",
                    "passingScore": 0,
                    "questions": "Is diluc cute?",
                    "quizID": 6,
                    "startDate": "03 Jan 2021"
                },
                {
                    "answers": "True",
                    "duration": 10,
                    "endDate": "21 Dec 2021",
                    "passingScore": 0,
                    "questions": "Is diluc cute?",
                    "quizID": 7,
                    "startDate": "07 Feb 2021"
                },
                {
                    "answers": "True",
                    "duration": 10,
                    "endDate": "21 Dec 2021",
                    "passingScore": 0,
                    "questions": "Is zhongli cute?",
                    "quizID": 8,
                    "startDate": "07 Feb 2021"
                },
                {
                    "answers": "True",
                    "duration": 10,
                    "endDate": "28 Feb 2022",
                    "passingScore": 0,
                    "questions": "Is zhongli cute?",
                    "quizID": 9,
                    "startDate": "21 Dec 2021"
                }
            ]
        }
        self.assertEqual(code, 200)
        self.assertEqual(json_data, check_data)





if __name__ == "__main__":
    unittest.main()
