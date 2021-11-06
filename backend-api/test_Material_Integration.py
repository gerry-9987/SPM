import unittest
from material import app, db

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

class MaterialTestCase(TestingApp):

    def test_get_all_materials(self):
        material_endpoint = "/material"
        response = self.client().get(material_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
        check_data = {
            "material": [
                {
                    "chapterID": 1,
                    "classID": 1,
                    "courseID": 1,
                    "materialID": 1,
                    "materialLink": "https://cseweb.ucsd.edu/classes/sp15/cse190-c/reports/sp15/048.pdf",
                    "materialLinkBody": "Predicting if income exceeds $50,000 per year based on 1994 US Census Data with\nSimple Classification Techniques",
                    "materialName": "Census Income",
                    "materialType": "document"
                },
                {
                    "chapterID": 2,
                    "classID": 1,
                    "courseID": 1,
                    "materialID": 2,
                    "materialLink": "https://www.google.com/",
                    "materialLinkBody": "You can learn more about google",
                    "materialName": "About google",
                    "materialType": "link"
                },
                {
                    "chapterID": 3,
                    "classID": 1,
                    "courseID": 1,
                    "materialID": 3,
                    "materialLink": "https://www.youtube.com/embed/mFFXuXjVgkU",
                    "materialLinkBody": "Everything you need to know to get started",
                    "materialName": "Github Actions CI/CD",
                    "materialType": "video"
                },
                {
                    "chapterID": 4,
                    "classID": 1,
                    "courseID": 1,
                    "materialID": 4,
                    "materialLink": "https://www.youtube.com/embed/yfoY53QXEnI",
                    "materialLinkBody": "We will be looking at styles, selectors, declarations, etc. We will build a CSS cheat sheet that you can keep as a resource and we will also create a basic website layout. ",
                    "materialName": "CSS Crash Course For Absolute Beginners",
                    "materialType": "video"
                }
            ]
        }
        self.assertEqual(code, 200)
        self.assertEqual(data, check_data)

    def test_get_material_by_chapter_success(self):
        material_by_chapter_endpoint = "/material/1"
        response = self.client().get(material_by_chapter_endpoint)
        code = response.status_code
        # decode bytes to string
        data = json.loads(response.data.decode("utf-8").replace("'", "\""))["data"]
        check_data = [
            {
                "chapterID": 1,
                "classID": 1,
                "courseID": 1,
                "materialID": 1,
                "materialLink": "https://cseweb.ucsd.edu/classes/sp15/cse190-c/reports/sp15/048.pdf",
                "materialLinkBody": "Predicting if income exceeds $50,000 per year based on 1994 US Census Data with\nSimple Classification Techniques",
                "materialName": "Census Income",
                "materialType": "document"
            }
        ]
        self.assertEqual(code, 200)
        self.assertEqual(data, check_data)

    def test_get_material_by_chapter_failure(self):
        material_by_chapter_endpoint = "/material/20"
        response = self.client().get(material_by_chapter_endpoint)
        code = response.status_code
        # decode bytes to string
        message = json.loads(response.data.decode("utf-8").replace("'", "\""))["message"]
        check_message = "Materials not found."
        self.assertEqual(code, 404)
        self.assertEqual(message, check_message)
        
    def test_add_new_material_success(self):
        request_body = {
            "chapterID": 2,
            "classID": 2,
            "courseID": 1,
            "materialID": 5,
            "materialLink": "https://www.helpguide.org/articles/sleep/getting-better-sleep.htm",
            "materialLinkBody": "How to improve on sleepy",
            "materialName": "Sleep",
            "materialType": "link"
        }
        create_material_endpoint = "/material"
        response = self.client().post(create_material_endpoint,
                                    data=json.dumps(request_body),
                                    content_type="application/json")
        response_code = response.json["code"]
        response_data = response.json["data"]
        self.assertEqual(response_code, 201)
        self.assertEqual(response_data,
            {
                "chapterID": 2,
                "classID": 2,
                "courseID": 1,
                "materialID": 5,
                "materialLink": "https://www.helpguide.org/articles/sleep/getting-better-sleep.htm",
                "materialLinkBody": "How to improve on sleepy",
                "materialName": "Sleep",
                "materialType": "link"
            }
        )

    def test_add_new_material_failure(self):
        request_body = {
            "chapterID": 2,
            "classID": 1,
            "courseID": 1,
            "materialID": 1,
            "materialLink": "https://www.helpguide.org/articles/sleep/getting-better-sleep.htm",
            "materialLinkBody": "How to improve on sleep",
            "materialName": "Sleep",
            "materialType": "link"
        }
        create_material_endpoint = "/material"
        response = self.client().post(create_material_endpoint,
                                    data=json.dumps(request_body),
                                    content_type="application/json")
        response_code = response.json["code"]
        response_message = response.json["message"]
        self.assertEqual(response_code, 500)
        self.assertEqual(response_message, "Material already exists.")

    def test_update_material_success(self):
        request_body = {
            "chapterID": 3,
            "classID": 1,
            "courseID": 1,
            "materialID": 3,
            "materialLink": "https://www.helpguide.org/articles/sleep/getting-better-sleep.htm",
            "materialLinkBody": "How to improve on sleep",
            "materialName": "Sleep",
            "materialType": "link"
        }
        update_material_endpoint = "/material"
        response = self.client().put(update_material_endpoint,
                                    data=json.dumps(request_body),
                                    content_type="application/json")
        response_code = response.json["code"]
        response_data = response.json["data"]
        self.assertEqual(response_code, 200)
        self.assertEqual(response_data,
            {
                "chapterID": 3,
                "classID": 1,
                "courseID": 1,
                "materialID": 3,
                "materialLink": "https://www.helpguide.org/articles/sleep/getting-better-sleep.htm",
                "materialLinkBody": "How to improve on sleep",
                "materialName": "Sleep",
                "materialType": "link"
            }
        )

    def test_update_material_failure(self):
        request_body = {
            "chapterID": 6,
            "classID": 1,
            "courseID": 3,
            "materialID": 6,
            "materialLink": "https://www.helpguide.org/articles/sleep/getting-better-sleep.htm",
            "materialLinkBody": "How to improve on sleep",
            "materialName": "Sleep",
            "materialType": "link"
        }
        update_material_endpoint = "/material"
        response = self.client().put(update_material_endpoint,
                                    data=json.dumps(request_body),
                                    content_type="application/json")
        response_code = response.json["code"]
        response_message = response.json["message"]
        self.assertEqual(response_code, 500)
        self.assertEqual(response_message, "Material does not exist yet."
        )


if __name__ == "__main__":
    unittest.main()