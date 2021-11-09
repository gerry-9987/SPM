from os import error
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

from dbModel import *

app = Flask(__name__)

import decouple
from decouple import config

db_password = config("DB_PASSWORD")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:' + db_password + '@spm-g8t9-db.cdlmqct6kw9s.us-east-1.rds.amazonaws.com:3306/spm_proj'

# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)


# get the list of all classes
@app.route("/class")
def get_all():

    class_list = Class.query.all()
    if len(class_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "classes": [a_class.json() for a_class in class_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no classes."
        }
    ), 404


# get classes for specific course
@app.route("/classes/<string:courseID>")
def get_classes(courseID):


    classRows = Class.query.filter_by(courseID=courseID).all() 
    if len(classRows) > 0:
        allClasses = [
            {
            "classID": eachClass.classID,
            "courseID": eachClass.courseID,
            "startDate": str(eachClass.startDate),
            "endDate": str(eachClass.endDate),
            "startTime": eachClass.startTime,
            "endTime": eachClass.endTime,
            "classSize": eachClass.classSize,
            "trainerName": eachClass.trainerName,
            "staffID": eachClass.staffID,
            "quizID":eachClass.quizID
            }
        for eachClass in classRows]

        return jsonify(
            {
                "code": 200,
                "data": allClasses
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no classes for this course."
        }
    ), 404


@app.route("/class/<string:classID>")
def get_class(classID):

    a_class = Class.query.filter_by(classID=classID).first()
    if a_class:
        return jsonify(
            {
                "code": 200,
                "data": a_class.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no such class."
        }
    ), 404

# add new class
@app.route("/class", methods=['POST'])
def create_class():

# classID, courseID, startDate, endDate, startTime, endTime, classSize,  trainerName, staffID
    classID = request.json.get("classID")
    courseID = request.json.get("courseID")
    startDate = request.json.get("startDate")
    endDate = request.json.get("endDate")
    startTime = request.json.get("startTime")
    endTime = request.json.get("endTime")
    classSize = request.json.get("classSize")
    trainerName = request.json.get("trainerName")
    staffID = request.json.get("staffID")
    quizID = request.json.get("quizID")

    a_class = Class(
        classID=classID,
        courseID=courseID,
        startDate=startDate,
        endDate=endDate,
        startTime=startTime,
        endTime=endTime,
        classSize=classSize,
        trainerName=trainerName,
        staffID=staffID,
        quizID= quizID
    )
    findclass = Class.query.filter(Class.classID==classID, Class.courseID==courseID).first()

    if not findclass:
        db.session.add(a_class)
        db.session.commit()
        return jsonify(
            {
                "code": 201,
                "data": a_class.json()
            }
        ), 201
    else:
        return jsonify(
            {
                "code": 500,
                "message": "The class already exists in this course."
            }
        ), 500

# get quizzes from a specific class and course
# @app.route("/find_quizzes", methods=['POST'])
# def find_quizzes():

#     classID = request.json.get("classID")
#     courseID = request.json.get("courseID")

#     findclasses = Class.query.filter(Class.classID==classID, Class.courseID==courseID).all()
#     print(findclasses)
    
#     res = []
#     for findclass in findclasses:
#         res.append(findclass.quizID)


#     return jsonify(
#         {
#             "code": 200,
#             "data": res
#         }
#     ), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
