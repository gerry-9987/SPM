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


@app.route("/all/<string:staffID>")
def get_details(staffID):

    takenCourses = Take_Class.query.filter_by(staffID=staffID)
    takenCourses = [(takenCourse.courseID, takenCourse.classID) for takenCourse in takenCourses]
    print(takenCourses)
    allDetails = []
    # for each course that learner takes
    for takenCourse in takenCourses:
        courseID = takenCourse[0]
        classID = takenCourse[1]
        singleDetails = {}
        courseDetails = Course.query.filter(Course.courseID==courseID).first().json()
        print("courseDetails")
        print(courseDetails)
        for courseDetail in courseDetails:
            if courseDetail not in singleDetails:
                singleDetails[courseDetail] = courseDetails[courseDetail]
        classDetails = Class.query.filter(and_(Class.courseID==courseID, Class.classID==classID)).first().json()
        print("classDetails")
        print(classDetails)
        for classDetail in classDetails:
            if classDetail not in singleDetails:
                singleDetails[classDetail] = classDetails[classDetail]
        
        print(singleDetails)
        classChapters = ClassChapter.query.filter(
            and_(ClassChapter.courseID==courseID,
                ClassChapter.classID==classID)).all()
        if classChapters:
            chapterIDs = [classChapter.chapterID for classChapter in classChapters]
            print(chapterIDs)
            chapterList = []
            for chapterID in chapterIDs:
                print("I am inside chapterID", chapterID)
                materials = Material.query.filter(Material.chapterID==chapterID).all()
                materials = [material.json() for material in materials]
                print(materials)
                chapterDetails = Chapter.query.filter(Chapter.chapterID==chapterID).first().json()
                if "materials" not in chapterDetails:
                    chapterDetails["materials"] = materials
                chapterList.append(chapterDetails)
            if "chapters" not in singleDetails:
                singleDetails["chapters"] = chapterList

        else:
            if "chapters" not in singleDetails:
                singleDetails["chapters"] = "There are no chapters for this class in this course."
        allDetails.append(singleDetails)

    return jsonify(
        {
            "code": 200,
            "data": allDetails
        }
    )
    
@app.route("/all", methods=['POST'])
def get_details2():
    
    
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
    return jsonify(
        {
            "code": 200,
            "data": res
        }
    ) 

if __name__ == '__main__':
    app.run(port=5011, debug=True)
