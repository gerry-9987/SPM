#Trainer Test lead by Ley Yi (refer to Trainer Integration Test, Staff Test, Staff Integration Test, Learner Test and Learner Integration Test too)

import unittest
from dbModel import *

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