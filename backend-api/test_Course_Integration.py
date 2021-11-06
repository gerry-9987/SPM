# %%
import unittest
import flask_testing
import json
from dbModel import Course
from course import *


class TestApp(flask_testing.TestCase):
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/spm_proj'
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestCourse(TestApp):

    def test_add_course_success(self):

        request_body = {
            'courseID': 555,
            'courseCategory': 'IS',
            'courseName': 'SPM',
            'courseDetails': 'Learn about software project management',
            'prereqCourses': 'IS111',
            'noOfClasses': 5,
            'students': '1,2,3,4,5'
        }

        response = self.client.post("/course",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json,
                         {
                             "code": 200,
                             "data": request_body
                         })
        
    def test_add_course_duplicated(self):

        request_body = {
            'courseID': 1,
            'courseCategory': 'IS',
            'courseName': 'SPM',
            'courseDetails': 'Learn about software project management',
            'prereqCourses': 'IS111',
            'noOfClasses': 5,
            'students': '1,2,3,4,5'
        }

        response = self.client.post("/course",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json,
                        {
                            "code": 300,
                            "message": "Course already exists"
                        })
    
        


if __name__ == '__main__':
    unittest.main()

# %%
