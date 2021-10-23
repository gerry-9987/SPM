from os import error
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/spm_proj'
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Quiz(db.Model):

    __tablename__ = 'quiz'
    quizID = db.Column(db.Integer(), primary_key=True, autoincrement=False)
    startDate = db.Column(db.VARCHAR(255), nullable=False)
    endDate = db.Column(db.VARCHAR(255), nullable=False)

    def __init__(self, quizID, startDate, endDate):
        self.quizID = quizID
        self.startDate = startDate
        self.endDate = endDate


    def json(self):
        return {
            "quizID": self.quizID,
            "startDate": self.startDate,
            "endDate": self.endDate
        }


# get the list of all staff
@app.route("/quiz")
def get_all():
    quizzes = Quiz.query.all()
    if len(quizzes):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "quiz": [quiz.json() for quiz in quizzes]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no quizzes."
        }
    ), 404


# get specific quiz
@app.route("/quiz/<string:quizID>")
def get_staff(quizID):
    quiz = Quiz.query.filter_by(quizID=quizID).first()
    if quiz:
        return jsonify(
            {
                "code": 200,
                "data": quiz.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Quiz is not found."
        }
    ), 404


# add new quiz
@app.route("/quiz", methods=['POST'])
def add_staff():


    quizID = request.json.get("quizID")
    startDate = request.json.get("startDate")
    endDate = request.json.get("endDate")

    quiz = Quiz(quizID=quizID, startDate=startDate, endDate=endDate)

    print(quiz.json())

    try:
        db.session.add(quiz)
        db.session.commit()
    except error:
        return jsonify(
            {
                "code": 500,
                "data": {
                },
                "message": "An error occurred adding the quiz."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": quiz.json()
        }
    ), 201


if __name__ == '__main__':
    app.run(port=5008, debug=True)
