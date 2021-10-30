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
import dbModel
from dbModel import Class


os.chdir("./backend-api")
# print(os.getcwd())
os.getcwd()


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


