#Quiz Class Unit Test lead by Geraldine (refer to Quiz Integration Test too)

import unittest

from dbModel import *
from quiz import app, db


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


if __name__ == "__main__":
    unittest.main()
