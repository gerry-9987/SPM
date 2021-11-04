# %%
import unittest
import flask_testing
import json
from dbModel import Course
from course import *


class TestApp(flask_testing.TestCase):
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
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

    # Test if adding new course works properly
    def test_add_course(self):
        # c1 = Course(courseID=100, courseName='SPM', courseCategory='IS',
        #             courseDetails='Learn about software project management', prereqCourses='IS111', noOfClasses=5, students='1,2,3,4,5')
        # db.session.add(c1)
        # db.session.commit()

        request_body = {
            'courseID': 101110,
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
        def test_get_course(self):
            # c1 = Course(courseID=100, courseName='SPM', courseCategory='IS',
            #             courseDetails='Learn about software project management', prereqCourses='IS111', noOfClasses=5, students='1,2,3,4,5')
            # db.session.add(c1)
            # db.session.commit()

            request_body = {
                'courseID': 101110,
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
        
        


if __name__ == '__main__':
    unittest.main()

# %%
