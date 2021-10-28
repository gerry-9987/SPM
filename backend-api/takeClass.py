from os import error
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from class1 import Class
from staff import Staff

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/spm_proj'
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Take_Class(db.Model):

    __tablename__ = 'take_class'
    staffID = db.Column(db.Integer(), db.ForeignKey('staff.staffID'), primary_key=True, autoincrement=False)
    classID = db.Column(db.Integer(), db.ForeignKey('class.classID'), primary_key=True, nullable=False)
    courseName = db.Column(db.VARCHAR(255), nullable=False)
    courseID = db.Column(db.Integer(), db.ForeignKey('class.courseID'), primary_key=True, nullable=False)
    # courseID = db.Column(db.Integer(), primary_key=True, nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint(
            staffID, courseID, classID,
            ),
        db.ForeignKeyConstraint([courseID, classID],
            ['class.courseID','class.classID']),
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
@app.route("/take_class/<string:staffID>")
def get_class_taken(staffID):
    class_taken = Take_Class.query.filter_by(staffID=staffID).first()
    if class_taken:
        return jsonify(
            {
                "code": 200,
                "data": class_taken.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Class taken not found."
        }
    ), 404


# add new class taken
@app.route("/take_class", methods=['POST'])
def add_class_taken():

    # staffID = request.json.get("staffID")
    # courseID = request.json.get("courseID")
    # courseName = request.json.get("courseName")
    # classID = request.json.get("classID")

    #hardcode test
    staffID =54
    courseID = 123
    courseName = "test"
    classID =321


    class_taken = Take_Class(staffID=staffID, courseID=courseID, courseName = courseName, classID=classID)

    print(class_taken.json())

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
            "code": 201,
            "data": class_taken.json()
        }
    ), 201


if __name__ == '__main__':
    app.run(port=5007, debug=True)
