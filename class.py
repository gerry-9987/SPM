from os import error
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
# import time
# import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/spm_proj'
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)


class Class():
    __tablename__ = 'class'

    def defaultconverter(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()

    classID = db.Column(db.Integer(), primary_key=True, nullable=False)
    courseID = db.Column(db.Integer(), db.ForeignKey('course.courseID'), primary_key=True, nullable=False)
    # startDate = db.Column(db.DateTime, nullable=False, default=defaultconverter)
    # endDate = db.Column(db.DateTime, nullable=False, default=defaultconverter)
    # startTime = db.Column(db.DateTime, nullable=False, default=defaultconverter)
    # endTime = db.Column(db.DateTime, nullable=False, default=defaultconverter)
    startDate = db.Column(db.DateTime, nullable=False, default=datetime.now)
    endDate = db.Column(db.DateTime, nullable=False, default=datetime.now)
    startTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    endTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    classSize = db.Column(db.Integer(), nullable=False)
    trainerName = db.Column(db.VARCHAR(255), nullable=False)
    staffID = db.Column(db.Integer(), db.ForeignKey('staff.staffID'), nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint(
            courseID, classID,
            ),
    )

    def __init__(self, classID, courseID, startDate, endDate, startTime, endTime, classSize,  trainerName, staffID):
        self.classID = classID
        self.courseID = courseID
        self.startDate = startDate
        self.endDate = endDate
        self.startTime = startTime
        self.endTime = endTime
        self.classSize = classSize
        self.trainerName = trainerName
        self.staffID = staffID

    def json(self):
        return {
            "classID": self.classID,
            "courseID": self.courseID,
            "startDate": self.startDate,
            "endDate": self.endDate,
            "startTime": self.startTime,
            "endTime": self.endTime,
            "classSize": self.classSize,
            "trainerName": self.trainerName,
            "staffID": self.staffID
        }

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


# get specific class
@app.route("/course/<string:classID>")
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
            "message": "Class not found."
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

    a_class = Class(
        classID=classID,
        courseID=courseID,
        startDate=startDate,
        endDate=endDate,
        startTime=startTime,
        endTime=endTime,
        classSize=classSize,
        trainerName=trainerName,
        staffID=staffID
    )

    print(a_class.json())

    try:
        db.session.add(a_class)
        db.session.commit()
    except error:
        return jsonify(
            {
                "code": 500,
                "data": {
                },
                "message": "An error occurred creating the class."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": a_class.json()
        }
    ), 201


if __name__ == '__main__':
    app.run(port=5003, debug=True)
    # app.run(host='0.0.0.0', port=5000, debug=True)
