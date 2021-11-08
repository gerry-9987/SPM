#Staff Test lead by Ley Yi (refer to Staff Integration Test, Learner Test, Learner Integration Test, Trainer Test and Trainer Integration Test too)

import unittest
from dbModel import *
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