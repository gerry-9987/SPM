import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

# import pytest
from os import error
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

# from .. import dbModel
from dbModel import Class


class TestClass(unittest.TestCase):
    def setUp(self):
        self.__class175 = dbModel.Class("1, 175, '01 Feb 2022', '01 May 2022', '10:00:00', '12:00:00', 20, 'Haoyue', 3, 175")

    def tearDown(self):
        self.__class175 = None

    def test_get(self):
        print("Hello")

# class TestClass(unittest.TestCase):

#     engine = create_engine('sqlite:///:memory:')
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     def setUp(self):
#         Class.metadata.create_all(self.engine)
#         self.session.add(dbModel.Class("1, 175, '01 Feb 2022', '01 May 2022', '10:00:00', '12:00:00', 20, 'Haoyue', 3, 175"))
#         self.session.commit()

#     def tearDown(self):
#         dbModel.Class.metadata.drop_all(self.engine)

#     def test_query_panel(self):
#         self.assertEqual("hello", "hello")
        # expected = [dbModel.Class("1, 175, '01 Feb 2022', '01 May 2022', '10:00:00', '12:00:00', 20, 'Haoyue', 3, 175")]
        # result = self.session.query(dbModel.Class).all()
        # self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()


#the other onee

import requests
import unittest
from unittest import mock
from dbModel import Class

# This is the class we want to test
# class MyGreatClass:
#     def fetch_json(self, url):
#         response = requests.get(url)
#         return response.json()

# This method will be used by the mock to replace requests.get
def mocked_requests_get():

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    # if url == '/class':

    return MockResponse({
                "code": 200,
                "data": {
                    "classes": [
                    {
                        "classID": 1,
                        "classSize": 4,
                        "courseID": 1,
                        "endDate": "03 Feb 2021",
                        "endTime": "23:30:00",
                        "staffID": 3,
                        "startDate": "01 Jan 2021",
                        "startTime": "22:30:00",
                        "trainerName": "Haoyue"
                    },
                    {
                        "classID": 2,
                        "classSize": 4,
                        "courseID": 1,
                        "endDate": "03 Feb 2021",
                        "endTime": "01:30:00",
                        "staffID": 3,
                        "startDate": "01 Jan 2021",
                        "startTime": "12:30:00",
                        "trainerName": "Haoyue"
                    },
                    {
                        "classID": 3,
                        "classSize": 4,
                        "courseID": 2,
                        "endDate": "07 May 2021",
                        "endTime": "02:30:00",
                        "staffID": 3,
                        "startDate": "03 Feb 2021",
                        "startTime": "01:30:00",
                        "trainerName": "Haoyue"
                    },
                    {
                        "classID": 4,
                        "classSize": 4,
                        "courseID": 2,
                        "endDate": "07 May 2021",
                        "endTime": "03:30:00",
                        "staffID": 3,
                        "startDate": "03 Feb 2021",
                        "startTime": "02:30:00",
                        "trainerName": "Haoyue"
                    },
                    {
                        "classID": 5,
                        "classSize": 4,
                        "courseID": 2,
                        "endDate": "07 May 2021",
                        "endTime": "23:30:00",
                        "staffID": 4,
                        "startDate": "03 Feb 2021",
                        "startTime": "22:30:00",
                        "trainerName": "Jewel"
                    },
                    {
                        "classID": 6,
                        "classSize": 4,
                        "courseID": 2,
                        "endDate": "07 May 2021",
                        "endTime": "02:30:00",
                        "staffID": 4,
                        "startDate": "03 Feb 2021",
                        "startTime": "12:30:00",
                        "trainerName": "Jewel"
                    },
                    {
                        "classID": 7,
                        "classSize": 4,
                        "courseID": 3,
                        "endDate": "07 May 2021",
                        "endTime": "02:30:00",
                        "staffID": 4,
                        "startDate": "04 Mar 2021",
                        "startTime": "01:30:00",
                        "trainerName": "Jewel"
                    }
                    ]
                }
                }, 200)

    # if url == 'http://someurl.com/test.json':
    #     return MockResponse({"key1": "value1"}, 200)
    # elif args[0] == 'http://someotherurl.com/anothertest.json':
    #     return MockResponse({"key2": "value2"}, 200)

    return MockResponse(None, 404)

# Our test case class
class TestingApp(unittest.TestCase):

    # We patch 'requests.get' with our own method. The mock object is passed in to our test case method.
    @mock.patch('dbModel.requests.get', side_effect=mocked_requests_get)
    def test_fetch(self, mock_get):
        # Assert requests.get calls
        # mgc = MyGreatClass()
        mgc = Class()
        json_data = mgc.fetch_json('/class')
        self.assertEqual(json_data, {
                    "code": 200,
                    "data": {
                        "classes": [
                        {
                            "classID": 1,
                            "classSize": 4,
                            "courseID": 1,
                            "endDate": "03 Feb 2021",
                            "endTime": "23:30:00",
                            "staffID": 3,
                            "startDate": "01 Jan 2021",
                            "startTime": "22:30:00",
                            "trainerName": "Haoyue"
                        },
                        {
                            "classID": 2,
                            "classSize": 4,
                            "courseID": 1,
                            "endDate": "03 Feb 2021",
                            "endTime": "01:30:00",
                            "staffID": 3,
                            "startDate": "01 Jan 2021",
                            "startTime": "12:30:00",
                            "trainerName": "Haoyue"
                        },
                        {
                            "classID": 3,
                            "classSize": 4,
                            "courseID": 2,
                            "endDate": "07 May 2021",
                            "endTime": "02:30:00",
                            "staffID": 3,
                            "startDate": "03 Feb 2021",
                            "startTime": "01:30:00",
                            "trainerName": "Haoyue"
                        },
                        {
                            "classID": 4,
                            "classSize": 4,
                            "courseID": 2,
                            "endDate": "07 May 2021",
                            "endTime": "03:30:00",
                            "staffID": 3,
                            "startDate": "03 Feb 2021",
                            "startTime": "02:30:00",
                            "trainerName": "Haoyue"
                        },
                        {
                            "classID": 5,
                            "classSize": 4,
                            "courseID": 2,
                            "endDate": "07 May 2021",
                            "endTime": "23:30:00",
                            "staffID": 4,
                            "startDate": "03 Feb 2021",
                            "startTime": "22:30:00",
                            "trainerName": "Jewel"
                        },
                        {
                            "classID": 6,
                            "classSize": 4,
                            "courseID": 2,
                            "endDate": "07 May 2021",
                            "endTime": "02:30:00",
                            "staffID": 4,
                            "startDate": "03 Feb 2021",
                            "startTime": "12:30:00",
                            "trainerName": "Jewel"
                        },
                        {
                            "classID": 7,
                            "classSize": 4,
                            "courseID": 3,
                            "endDate": "07 May 2021",
                            "endTime": "02:30:00",
                            "staffID": 4,
                            "startDate": "04 Mar 2021",
                            "startTime": "01:30:00",
                            "trainerName": "Jewel"
                        }
                        ]
                    }
                    })
        # json_data = mgc.fetch_json('http://someotherurl.com/anothertest.json')
        # self.assertEqual(json_data, {"key2": "value2"})
        json_data = mgc.fetch_json('http://nonexistenturl.com/cantfindme.json')
        self.assertIsNone(json_data)

        # We can even assert that our mocked method was called with the right parameters
        self.assertIn(mock.call('/class'), mock_get.call_args_list)
        self.assertIn(mock.call('/class'), mock_get.call_args_list)

        # self.assertEqual(len(mock_get.call_args_list), 3)

if __name__ == '__main__':
    unittest.main()



