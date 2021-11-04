import unittest

from dbModel import *
from quiz import app, db

import json
from ast import literal_eval


class TestingApp(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

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

class QuizTestCase(TestingApp):
    def test_get_all_quizzes(self):
        quiz_endpoint = "/quiz"
        response = self.client().get(quiz_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
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
        self.assertEqual(data, check_data)

    def test_get_specific_quiz(self):
        quiz_by_id_endpoint = "/quiz/1"
        response = self.client().get(quiz_by_id_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
        check_data = {
            "answers": "True, True, True, True, False, True, False, True",
            "duration": 100,
            "endDate": "03 Jan 2021",
            "passingScore": 50,
            "questions": "Is cat cute?, Is dog cute?, Does SPM teach pair programming?, Do chickens lay eggs?, Can chickens swim?, Can monkeys dance?, Can birds talk?, Is this module fun?",
            "quizID": 1,
            "startDate": "01 Jan 2021"
        }
        self.assertEqual(code, 200)
        self.assertEqual(data, check_data)

    def test_get_specific_questions(self):
        questions_by_quizid_endpoint = "/quiz/1/questions"
        response = self.client().get(questions_by_quizid_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
        check_data = [
            "Is cat cute?", 
            "Is dog cute?", 
            "Does SPM teach pair programming?", 
            "Do chickens lay eggs?",
            "Can chickens swim?", 
            "Can monkeys dance?", 
            "Can birds talk?", 
            "Is this module fun?"
        ]
        self.assertEqual(code, 200)
        self.assertEqual(data, check_data)

    def test_get_specific_answers(self):
        answers_by_quizid_endpoint = "/quiz/1/answers"
        response = self.client().get(answers_by_quizid_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
        check_data = [
            "True", 
            "True", 
            "True", 
            "True", 
            "False", 
            "True", 
            "False", 
            "True"
        ]
        self.assertEqual(code, 200)
        self.assertEqual(data, check_data)

    # def test_create_quiz(self):
    #     request_body = {
    #         "quizID": 116,
    #         "startDate": "01 Jan 2021",
    #         "endDate": "03 Jan 2021",
    #         "questions": "Happy?, Sad?",
    #         "answers": "True, False",
    #         "duration": 10,
    #         "passingScore": 0
    #     }

    #     create_quiz_endpoint = "/quiz/create"
    #     response = self.client().post(create_quiz_endpoint,
    #                                 data=json.dumps(request_body),
    #                                 content_type='application/json' )

    #     self.assertEqual(response.json, {
    #         "code": 200,
    #         "message": "Quiz has been created."
    #     })


if __name__ == "__main__":
    unittest.main()
