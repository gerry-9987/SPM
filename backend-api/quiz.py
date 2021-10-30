from os import error
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from dbModel import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/spm_proj'
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)



# get the list of all quizzes
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
def get_quiz(quizID):
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


# get questions in a specific quiz
@app.route("/quiz/questions/<string:quizID>")
def get_questions(quizID):
    quizzes = Quiz.query.filter_by(quizID=quizID)

    if quizzes:
        questions = [quiz.question for quiz in quizzes]
        return jsonify(
            {
                "code": 200,
                "data": questions
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Quiz is not found."
        }
    ), 404

# add new quiz
@app.route("/quiz/create", methods=['POST'])
def add_quiz():
    
    quizID = request.json.get("quizID")
    startDate = request.json.get("startDate")
    endDate = request.json.get("endDate")
    question = request.json.get("question")
    answer = request.json.get("answer")

    quiz = Quiz(quizID=quizID, startDate=startDate, endDate=endDate, question=question, answer=answer)

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
            "code": 200,
            "message": "Quiz has been created."
        }
    ), 201


if __name__ == '__main__':
    app.run(port=5008, debug=True)
