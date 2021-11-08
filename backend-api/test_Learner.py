#Learner Test lead by Ley Yi (refer to Learner Integration Test, Staff Test, Staff Integration Test, Trainer Test and Trainer Integration Test too)

import unittest
from dbModel import *

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