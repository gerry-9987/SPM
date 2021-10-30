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

# get the list of all graded quizzes
@app.route("/gradedquiz")
def get_all():
    graded_quizzes = GradedQuiz.query.all()
    if len(graded_quizzes):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "quiz": [gradedquiz.json() for gradedquiz in graded_quizzes]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no graded quizzes."
        }
    ), 404


# get specific graded quiz
@app.route("/gradedquiz/<string:quizID>")
def get_graded_quiz(quizID):
    gradedquiz = Quiz.query.filter_by(quizID=quizID).first()
    if gradedquiz:
        return jsonify(
            {
                "code": 200,
                "data": gradedquiz.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Graded Quiz is not found."
        }
    ), 404

# add new graded quiz
@app.route("/gradedquiz", methods=['POST'])
def add_graded_quiz():

    quizID = request.json.get("quizID")
    passingScore = request.json.get("passingScore")
    gradedquiz = GradedQuiz(quizID=quizID, passingScore=passingScore)

    try:
        db.session.add(gradedquiz)
        db.session.commit()
    except error:
        return jsonify(
            {
                "code": 500,
                "data": {
                },
                "message": "An error occurred adding the graded quiz."
            }
        ), 500

    return jsonify(
        {
            "code": 200,
            "message": "Graded has been added."
        }
    ), 201


if __name__ == '__main__':
    app.run(port=5009, debug=True)
