from os import error
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from dbModel import *

from sqlalchemy import and_

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/spm_proj'
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)


@app.route("/all", methods=['POST'])
def get_details():
    print("I am inside get all details")

    classID = request.json.get("classID")
    courseID = request.json.get("courseID")

    res = {'chapters':[],'quizIDs':[],'materials':[]}

    # Get chapter details
    course = Course.query.filter(Course.courseID==courseID).first()
    res['courseName'] = course.courseName
    res['courseDetails'] = course.courseDetails
    print(res)

    # Get all the quizIDs
    chapters = ClassChapter.query.filter(ClassChapter.courseID==courseID, ClassChapter.classID==classID).all()
    for chapter in chapters:
        print(chapter.json())
        res['chapters'].append(chapter.chapterID)
        res['quizIDs'].append(chapter.quizID)

    # Get all the materials
    materials = Material.query.filter(Material.courseID==courseID, Material.classID==classID).all()
    for material in materials:
        print(material.json())
        res['materials'].append(material.json())

    # Return
    return jsonify(
        {
            "code": 200,
            "data": res
        }
    ) 

if __name__ == '__main__':
    app.run(port=5011, debug=True)
