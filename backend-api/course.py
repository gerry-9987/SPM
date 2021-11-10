from os import error
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dbModel import *
import decouple
from decouple import config

db_url=config("DB_URL")
db_password = config("DB_PASSWORD")
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:' + db_password + db_url

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

# get the list of all courses

@app.route("/course")
def get_all():
    course_list = Course.query.all()
    if len(course_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "courses": [course.json() for course in course_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no courses."
        }
    ), 404


# get specific course details
@app.route("/course/<string:courseID>")
def get_course_details(courseID):

    course = Course.query.filter_by(courseID=courseID).first()
    if course:
        return jsonify(
            {
                "code": 200,
                "data": course.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Course not found." 
        }
    ), 404


@app.route("/courses/<string:staffID>")
def get_learner_courses(staffID):
    takenCourses = Take_Class.query.filter_by(staffID=staffID)
    takenCourses = [takenCourse.courseID for takenCourse in takenCourses]

    courses = Course.query.filter(Course.courseID.in_(takenCourses)).all()
    if len(courses) > 0:
        return jsonify(
            {
                "code": 200,
                "data": [course.json() for course in courses]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No courses are taken by this learner"
        }
    )

# add new course
@app.route("/course", methods=['POST'])
def create_course():

    courseID = request.json.get("courseID")
    courseName = request.json.get("courseName")
    courseCategory = request.json.get("courseCategory")
    courseDetails = request.json.get("courseDetails")
    prereqCourses = request.json.get("prereqCourses")
    noOfClasses = request.json.get("noOfClasses")
    students = request.json.get("students")

    course = Course(
        courseID=courseID,
        courseName=courseName,
        courseCategory=courseCategory,
        courseDetails=courseDetails,
        prereqCourses=prereqCourses,
        noOfClasses=noOfClasses,
        students=students)

    print(course)
    course_exists = Course.query.filter_by(courseName=courseName).first()
    if course_exists: return jsonify(
        {
            "code": 300,
            "message":"Course already exists"
        }
    ), 300


    print(course.json())

    try:
        db.session.add(course)
        db.session.commit()
    except error:
        return jsonify(
            {
                "code": 500,
                "data": {
                },
                "message": "An error occurred creating the course."
            }
        ), 500

    return jsonify(
        {
            "code": 200,
            "data": course.json()
        }
    ), 200

# Sign up
# TODO: Test this method
@app.route("/signup", methods=['POST'])
def signup():

    # Get POST variables
    courseID = request.json.get("courseID")
    studentID = request.json.get("studentID")

    # Update row in DB
    course = Course.query.filter_by(courseID=courseID).first()
    course.addStudent(studentID)

    try:
        db.session.commit()
    except error:
        return jsonify(
            {
                "code": 500,
                "data": {
                },
                "message": "An error occurred during sign up."
            }
        ), 500

    return jsonify(
        {
            "code": 200,
            "data": course.json()
        }
    ), 200


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5001, debug=True)
    app.run(host='0.0.0.0', port=5003, debug=True)
