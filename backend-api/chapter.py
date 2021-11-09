import os
from os import cpu_count, error
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import and_
import decouple
from decouple import config

db_url=config("DB_URL")
db_password = config("DB_PASSWORD")

from dbModel import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:' + db_password + db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)


# get the list of all chapters
@app.route("/chapter")
def get_all_chapters():
    chapter_list = Chapter.query.all()
    if len(chapter_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "chapters": [chapter.json() for chapter in chapter_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no chapters."
        }
    ), 404


# get specific chapter
@app.route("/chapter/<string:chapterID>")
def get_chapter(chapterID):
    chapter = Chapter.query.filter_by(chapterID=chapterID).first()
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


# get chapters by course
@app.route("/chapter/course/<string:courseID>")
def get_course_chapters(courseID):
    classes = Class.query.filter_by(courseID=courseID).all()
    classIDs = [a_class.classID for a_class in classes]
    chapters = ClassChapter.query.filter(ClassChapter.classID.in_(classIDs)).all()
    chapterIDs = [chapter.chapterID for chapter in chapters]
    allChapters = Chapter.query.filter(Chapter.chapterID.in_(chapterIDs)).all()
    if allChapters:
        return jsonify(
            {
                "code": 200,
                "data": [chapter.json() for chapter in allChapters]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Chapters not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
