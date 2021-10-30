import unittest

import sys

# from dbModel import *
import os
sys.path.append(os.path.abspath("\wamp64\www\SPM\SPM\backend-api"))
# print(sys.path)
# sys.path.append('./')

import dbModel
from dbModel import *
import quiz
from quiz import *

class test_Quiz(unittest.TestCase):
    def setUp(self):
        self.quiz = Quiz(7, '01 Jan 2021', '03 Jan 2021', 'Is cat cute?', 'True')

    def tearDown(self):
        self.quiz = None

    def test_quiz_details(self):
        quizDetails = self.quiz.json()
        self.assertEqual(quizDetails, {
            "quizID": 7,
            "startDate": '01 Jan 2021',
            "endDate": '03 Jan 2021',
            "question": 'Is cat cute?',
            "answer": 'True'}
        )

    # def test_quiz_details(self):

if __name__ == "__main__":
    unittest.main()
