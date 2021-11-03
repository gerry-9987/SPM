import unittest
from chapter import app, db

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

class ChapterTestCase(TestingApp):

    def test_get_all_chapters(self):
        chapter_endpoint = "/chapter"
        response = self.client().get(chapter_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
        check_data = {
            "chapters": [
                {
                    "chapterDetails": "A cat is running away",
                    "chapterID": 1,
                    "chapterName": "CAT",
                    "quizID": 1
                },
                {
                    "chapterDetails": "A dog is running away",
                    "chapterID": 2,
                    "chapterName": "DOG",
                    "quizID": 2
                },
                {
                    "chapterDetails": "A turtle is running away",
                    "chapterID": 3,
                    "chapterName": "TURTLE",
                    "quizID": 3
                },
                {
                    "chapterDetails": "My life is great",
                    "chapterID": 4,
                    "chapterName": "LIFE",
                    "quizID": 4
                },
                {
                    "chapterDetails": "A foetus is growing",
                    "chapterID": 5,
                    "chapterName": "foetus",
                    "quizID": 5
                },
                {
                    "chapterDetails": "A baby is crawling away",
                    "chapterID": 6,
                    "chapterName": "baby",
                    "quizID": 6
                },
                {
                    "chapterDetails": "yay diluc",
                    "chapterID": 7,
                    "chapterName": "diluc",
                    "quizID": 7
                },
                {
                    "chapterDetails": "yay zhongli",
                    "chapterID": 8,
                    "chapterName": "zhongli",
                    "quizID": 8
                },
                {
                    "chapterDetails": "yay cutest",
                    "chapterID": 9,
                    "chapterName": "cutest",
                    "quizID": 1
                },
                {
                    "chapterDetails": "yay cuter",
                    "chapterID": 10,
                    "chapterName": "cuter",
                    "quizID": 2
                },
                {
                    "chapterDetails": "AAA yummy",
                    "chapterID": 11,
                    "chapterName": "AAA",
                    "quizID": 3
                },
                {
                    "chapterDetails": "BBB happy",
                    "chapterID": 12,
                    "chapterName": "BBB",
                    "quizID": 4
                },
                {
                    "chapterDetails": "BBV bumble bee",
                    "chapterID": 13,
                    "chapterName": "BBV",
                    "quizID": 5
                },
                {
                    "chapterDetails": "CCC bumble bee",
                    "chapterID": 14,
                    "chapterName": "CCC",
                    "quizID": 6
                },
                {
                    "chapterDetails": "DDD bumble bee",
                    "chapterID": 15,
                    "chapterName": "DDD",
                    "quizID": 7
                },
                {
                    "chapterDetails": "EEE bumble bee",
                    "chapterID": 16,
                    "chapterName": "EEE",
                    "quizID": 8
                },
                {
                    "chapterDetails": "FFF bumble bee",
                    "chapterID": 17,
                    "chapterName": "FFF",
                    "quizID": 9
                },
                {
                    "chapterDetails": "GGG bumble bee",
                    "chapterID": 18,
                    "chapterName": "GGG",
                    "quizID": 9
                }
            ]
        }
        self.assertEqual(code, 200)
        self.assertEqual(data, check_data)
