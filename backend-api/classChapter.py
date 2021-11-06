from os import error
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import and_

from dbModel import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/spm_proj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)


# get the list of classes' chapters
@app.route("/class_chapter")
def get_all_class_chapters():
    class_chapter_list = ClassChapter.query.all()
    if len(class_chapter_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "chapters": [class_chapter.json() for class_chapter in class_chapter_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no class chapters."
        }
    ), 404


# get specific chapter
@app.route("/class_chapter/<string:chapterID>")
def get_class_chapter(chapterID):
    chapter = ClassChapter.query.filter_by(chapterID=chapterID).first()
    if chapter:
        return jsonify(
            {
                "code": 200,
                "data": chapter.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Chapter not found."
        }
    ), 404


# get specific course, class and its chapter
@app.route("/class_chapter/<string:courseID>/<string:classID>/<string:chapterID>")
def get_course_class_chapter(courseID, classID, chapterID):
    specific_chapter = ClassChapter.query.filter(
        and_(ClassChapter.courseID==courseID, \
            ClassChapter.classID==classID, \
            ClassChapter.chapterID==chapterID)
    ).first()
    if specific_chapter:
        return jsonify(
            {
                "code": 200,
                "data": specific_chapter.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Course {}'s Class {} does not have Chapter {}.".format(courseID, classID, chapterID)
        }
    ), 404

# get quizzes from a specific class and course
@app.route("/find_quizes", methods=['POST'])
def find_quizes():

    classID = request.json.get("classID")
    courseID = request.json.get("courseID")
    print(classID, courseID)

    findclasses = ClassChapter.query.filter(ClassChapter.classID==classID, ClassChapter.courseID==courseID).all()
    print(findclasses)
    
    res = []
    for findclass in findclasses:
        res.append(findclass.quizID)


    return jsonify(
        {
            "code": 200,
            "data": res
        }
    ), 200
    

if __name__ == '__main__':
    app.run(port=5001, debug=True)
