#%%

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import ForeignKeyConstraint, PrimaryKeyConstraint
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


class Chapter(db.Model):


    __tablename__ = 'CHAPTER'
    chapterID = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    chapterName = db.Column(db.VARCHAR(255), nullable=False)
    chapterDetails = db.Column(db.VARCHAR(255), nullable=False)
    quizID = db.Column(db.Integer(), db.ForeignKey('QUIZ.quizID'), nullable=False)

    def __init__(self, chapterID, chapterName, chapterDetails, quizID):
        self.chapterID = chapterID
        self.chapterName = chapterName
        self.chapterDetails = chapterDetails
        self.quizID = quizID


    def json(self):
        return {
            "chapterID": self.chapterID,
            "chapterName": self.chapterName,
            "chapterDetails": self.chapterDetails,
            "quizID": self.quizID
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Class(db.Model):


    __tablename__ = 'CLASS'
    classID = db.Column(db.Integer(), primary_key=True, nullable=False)
    courseID = db.Column(db.Integer(), db.ForeignKey('COURSE.courseID'), primary_key=True, nullable=False)
    startDate = db.Column(db.VARCHAR(255), nullable=False)
    endDate = db.Column(db.VARCHAR(255), nullable=False)
    startTime = db.Column(db.VARCHAR(255), nullable=False)
    endTime = db.Column(db.VARCHAR(255), nullable=False)
    classSize = db.Column(db.Integer(), nullable=False)
    trainerName = db.Column(db.VARCHAR(255), nullable=False)
    staffID = db.Column(db.Integer(), db.ForeignKey('STAFF.staffID'), nullable=False)
    quizID = db.Column(db.Integer(), db.ForeignKey('QUIZ.quizID'), nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint(
            courseID, classID,
            ),
    )

    def __init__(self, classID, courseID, startDate, endDate, startTime, endTime, classSize,  trainerName, staffID, quizID):
        self.classID = classID
        self.courseID = courseID
        self.startDate = startDate
        self.endDate = endDate
        self.startTime = startTime
        self.endTime = endTime
        self.classSize = classSize
        self.trainerName = trainerName
        self.staffID = staffID
        self.quizID = quizID

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
            "staffID": self.staffID,
            "quizID": self.quizID
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class ClassChapter(db.Model):


    __tablename__ = 'CLASS_CHAPTER'
    courseID = db.Column(db.Integer(), db.ForeignKey('CLASS.courseID'), primary_key=True, nullable=False)
    classID = db.Column(db.Integer(), db.ForeignKey('CLASS.classID'), primary_key=True, nullable=False)
    chapterID = db.Column(db.Integer(), db.ForeignKey('CHAPTER.chapterID'), primary_key=True, autoincrement=True)
    quizID = db.Column(db.Integer(), db.ForeignKey('QUIZ.quizID'), primary_key=True, autoincrement=True)

    def __init__(self, courseID, classID, chapterID, quizID):
        self.courseID = courseID
        self.classID = classID
        self.chapterID = chapterID
        self.quizID = quizID


    def json(self):
        return {
            "courseID": self.courseID,
            "classID": self.classID,
            "chapterID": self.chapterID,
            "quizID": self.quizID
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Course(db.Model):

    __tablename__ = 'COURSE'
    courseID = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    courseName = db.Column(db.VARCHAR(255), nullable=False)
    courseCategory = db.Column(db.VARCHAR(255), nullable=False)
    courseDetails = db.Column(db.VARCHAR(255), nullable=False)
    prereqCourses = db.Column(db.VARCHAR(255), nullable=False)
    noOfClasses = db.Column(db.Integer(), nullable=False)
    students = db.Column(db.VARCHAR(255), nullable=False)

    def __init__(self, courseID, courseName, courseCategory, courseDetails, prereqCourses, noOfClasses, students):
        self.courseID = courseID
        self.courseName = courseName
        self.courseCategory = courseCategory
        self.courseDetails = courseDetails
        self.prereqCourses = prereqCourses
        self.noOfClasses = noOfClasses
        self.students = students

    def json(self):
        return {
            "courseID": self.courseID,
            "courseName": self.courseName,
            "courseCategory": self.courseCategory,
            "courseDetails": self.courseDetails,
            "prereqCourses": self.prereqCourses,
            "noOfClasses": self.noOfClasses,
            "students": self.students
        }

    def addStudent(self, studentID):
        studentArray = self.students.split(",")
        print(studentID, studentArray)

        if str(studentID) not in studentArray:
            self.students = self.students + ',' + str(studentID)
        else:
            return "Student is already enrolled in this course"

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Learner(db.Model):


    __tablename__ = 'LEARNER'
    staffID = db.Column(db.Integer(), db.ForeignKey('STAFF.staffID'), primary_key=True, autoincrement=False)
    numberOfClassesPassed = db.Column(db.Integer(), nullable=False)

    def __init__(self, staffID, numberOfClassesPassed):
        self.staffID = staffID
        self.numberOfClassesPassed = numberOfClassesPassed


    def json(self):
        return {
            "staffID": self.staffID,
            "numberOfClassesPassed": self.numberOfClassesPassed,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Material(db.Model):


    __tablename__ = 'MATERIAL'
    materialID = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    materialName = db.Column(db.VARCHAR(255), nullable=False)
    materialType = db.Column(db.VARCHAR(255), nullable=False)
    materialLink = db.Column(db.VARCHAR(255), nullable=False)
    materialLinkBody = db.Column(db.VARCHAR(255), nullable=False)
    chapterID = db.Column(db.Integer(), db.ForeignKey('CHAPTER.chapterID'), nullable=False)
    classID = db.Column(db.Integer(), db.ForeignKey('CLASS.classID'), nullable=False)
    courseID = db.Column(db.Integer(), db.ForeignKey('CLASS.courseID'), nullable=False)


    def __init__(self, materialID, materialName, materialType, materialLink, materialLinkBody, chapterID, classID, courseID):
        self.materialID = materialID
        self.materialName = materialName
        self.materialType = materialType
        self.materialLink = materialLink
        self.materialLinkBody = materialLinkBody
        self.chapterID = chapterID
        self.classID = classID
        self.courseID = courseID

    def json(self):
        return {
            "materialID": self.materialID,
            "materialName": self.materialName,
            "materialType": self.materialType,
            "materialLink": self.materialLink,
            "materialLinkBody": self.materialLinkBody,
            "chapterID": self.chapterID,
            "classID": self.classID,
            "courseID": self.courseID
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Quiz(db.Model):


    __tablename__ = 'QUIZ'
    quizID = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    startDate = db.Column(db.VARCHAR(255), nullable=False)
    endDate = db.Column(db.VARCHAR(255), nullable=False)
    questions = db.Column(db.VARCHAR(255), nullable=False)
    answers = db.Column(db.VARCHAR(255), nullable=False)
    duration = db.Column(db.Integer(), nullable=False)
    passingScore = db.Column(db.Integer(), nullable=False)


    def __init__(self, quizID, startDate, endDate, questions, answers, duration, passingScore):
        self.quizID = quizID
        self.startDate = startDate
        self.endDate = endDate
        self.questions = questions
        self.answers = answers
        self.duration = duration
        self.passingScore = passingScore

    def json(self):
        return {
            "quizID": self.quizID,
            "startDate": self.startDate,
            "endDate": self.endDate,
            "questions": self.questions,
            "answers": self.answers,
            "duration": self.duration,
            "passingScore": self.passingScore
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

# class GradedQuiz(db.Model):


#     __tablename__ = 'gradedquiz'
#     quizID = db.Column(db.Integer(), primary_key=True, autoincrement=False)
#     passingScore = db.Column(db.Integer(), db.ForeignKey('quiz.quizID'), autoincrement=False)

#     def __init__(self, quizID, passingScore):
#         self.quizID = quizID
#         self.passingScore = passingScore

#     def json(self):
#         return {
#             "quizID": self.quizID,
#             "passingScore": self.passingScore
#         }

class LearnerQuiz(db.Model):


    __tablename__ = 'LEARNER_QUIZ'
    quizID = db.Column(db.Integer(), db.ForeignKey('QUIZ.quizID'), primary_key=True, autoincrement=False)
    staffID = db.Column(db.Integer(), db.ForeignKey('STAFF.staffID'), primary_key=True, autoincrement=False)
    quizScore = db.Column(db.Integer(), autoincrement=False)

    __table_args__ = (
    PrimaryKeyConstraint(
        quizID, staffID
        ),
    )

    def __init__(self, quizID, staffID, quizScore):
        self.quizID = quizID
        self.staffID = staffID
        self.quizScore = quizScore
        

    def json(self):
        return {
            "quizID": self.quizID,
            "staffID": self.staffID,
            "quizScore": self.quizScore
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Staff(db.Model):


    __tablename__ = 'STAFF'
    staffID = db.Column(db.Integer(), primary_key=True, autoincrement=False)
    staffUsername = db.Column(db.VARCHAR(255), nullable=False)
    staffName = db.Column(db.VARCHAR(255), nullable=False)
    department = db.Column(db.VARCHAR(255), nullable=False)

    def __init__(self, staffID, staffUsername, staffName, department):
        self.staffID = staffID
        self.staffUsername = staffUsername
        self.staffName = staffName
        self.department = department


    def json(self):
        return {
            "staffID": self.staffID,
            "staffUsername": self.staffUsername,
            "staffName": self.staffName,
            "department": self.department,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Take_Class(db.Model):


    __tablename__ = 'TAKE_CLASS'
    staffID = db.Column(db.Integer(), db.ForeignKey('STAFF.staffID'), primary_key=True, nullable=False, autoincrement=False)
    courseID = db.Column(db.Integer(), db.ForeignKey('CLASS.courseID'), primary_key=True, nullable=False, autoincrement=False)
    classID = db.Column(db.Integer(), db.ForeignKey('CLASS.classID'), primary_key=True, nullable=False, autoincrement=False)
    courseName = db.Column(db.VARCHAR(255), nullable=False)
    # courseID = db.Column(db.Integer(), primary_key=True, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint(
            staffID, courseID, classID,
            ),
        ForeignKeyConstraint(["staffID"], ['STAFF.staffID']),
        ForeignKeyConstraint(["courseID", "classID"],
            ['CLASS.courseID','CLASS.classID']),
    )

    def __init__(self, staffID, courseID, courseName, classID):
        self.staffID = staffID
        self.courseID = courseID
        self.courseName = courseName
        self.classID = classID

    def json(self):
        return {
            "staffID": self.staffID,
            "courseID": self.courseID,
            "courseName": self.courseName,
            "classID": self.classID
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Trainer(db.Model):


    __tablename__ = 'TRAINER'
    staffID = db.Column(db.Integer(), db.ForeignKey('STAFF.staffID'), primary_key=True, autoincrement=False)
    numberOfClasses = db.Column(db.Integer(), nullable=False)

    def __init__(self, staffID, numberOfClasses):
        self.staffID = staffID
        self.numberOfClasses = numberOfClasses


    def json(self):
        return {
            "staffID": self.staffID,
            "numberOfClasses": self.numberOfClasses,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


# %%
