from os import error
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/spm_proj'
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

import dbModel as dbModel
from dbModel import *
Take_Class = dbModel.Take_Class

# get the list of all classes taken
@app.route("/take_class")
def get_all():
    take_class_list = Take_Class.query.all()
    if len(take_class_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "classes_taken": [class_taken.json() for class_taken in take_class_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no classes taken."
        }
    ), 404


# get specific class taken
# @app.route("/take_class/<string:staffID>")
# def get_class_taken(staffID):
#     class_taken = Take_Class.query.filter_by(staffID=staffID).first()
#     if class_taken:
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": class_taken.json()
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "message": "Class taken not found."
#         }
#     ), 404

# @app.route("/take_class/course/<string:courseID>")
# def get_class_taken_course(courseID):
#     class_taken = Take_Class.query.filter_by(courseID=courseID).first()
#     if class_taken:
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": class_taken.json()
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "message": "Class taken not found."
#         }
#     ), 404

# add new class taken
@app.route("/take_class", methods=['POST'])
def add_class_taken():
    # {
    #     "staffID": 3,
    #     "courseID": 1,
    #     "courseName": "IBM 102",
    #     "classID": 2
    # }
    # print(request.json)
    staffID = request.json.get("staffID")
    print(staffID)
    courseID = request.json.get("courseID")
    courseName = request.json.get("courseName")
    classID = request.json.get("classID")

    #hardcode test
    # staffID =1
    # courseID = 1
    # courseName = "IBM 102"
    # classID =2

    # print(staffID, courseID, courseName, classID)

    class_taken = Take_Class(staffID, courseID, courseName, classID)

    findClassTaken = Take_Class.query.filter(Take_Class.staffID==staffID, Take_Class.courseID==courseID, Take_Class.classID==classID).first()
    if findClassTaken:
        return jsonify(
        {
            "code": 300,
            "message": 'already have this entry'
        }
    ), 300
        
    try:
        db.session.add(class_taken)
        db.session.commit()
    except error:
        return jsonify(
            {
                "code": 500,
                "data": {
                },
                "message": "An error occurred adding the class taken."
            }
        ), 500

    return jsonify(
        {
            "code": 200,
            "data": class_taken.json()
        }
    ), 200

# Withdraw from a class
@app.route("/withdraw", methods=['POST'])
def withdraw():

    staffID = request.json.get("staffID")
    courseID = request.json.get("courseID")
    courseName = request.json.get("courseName")
    classID = request.json.get("classID")

    class_taken = Take_Class(staffID, courseID, courseName, classID)

    findClassTaken = Take_Class.query.filter(Take_Class.staffID==staffID, Take_Class.courseID==courseID, Take_Class.classID==classID).first()
    if not findClassTaken:
        return jsonify(
        {
            "code": 300,
            "message": 'Not enrolled at the moment'
        }
    ), 300
        
    try:
        Take_Class.query.filter(Take_Class.staffID==staffID, Take_Class.courseID==courseID, Take_Class.classID==classID).delete()
        db.session.commit()
        
    except error:
        return jsonify(
            {
                "code": 500,
                "data": {
                },
                "message": "An error occurred withdrawing from the class."
            }
        ), 500

    return jsonify(
        {
            "code": 200,
            "data": class_taken.json()
        }
    ), 200

if __name__ == '__main__':
    app.run(port=5007, debug=True)
