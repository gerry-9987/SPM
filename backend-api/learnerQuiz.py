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

# get the list of all learner quizzes
@app.route("/learnerquiz")
def get_all():
    learner_quizzes = LearnerQuiz.query.all()
    if len(learner_quizzes):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "quiz": [learnerquiz.json() for learnerquiz in learner_quizzes]
                }
            }
        )
    return jsonify(
        {
            "code": 500,
            "message": "There are no learner quizzes."
        }
    ), 500


# get specific learner quiz
@app.route("/learnerquiz/<string:quizID>")
def get_learner_quiz(quizID):
    learnerquiz = LearnerQuiz.query.filter_by(quizID=quizID).first()
    if learnerquiz:
        return jsonify(
            {
                "code": 200,
                "data": learnerquiz.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Learner Quiz is not found."
        }
    ), 404

# add new learner quiz
@app.route("/learnerquiz", methods=['POST'])
def add_learner_quiz():

    quizID = request.json.get("quizID")
    staffID = request.json.get("staffID")
    quizScore = request.json.get("quizScore")
    learnerquiz = LearnerQuiz(quizID=quizID, staffID = staffID, quizScore=quizScore)

    try:
        db.session.add(learnerquiz)
        db.session.commit()
        
    except error:
        return jsonify(
            {
                "code": 500,
                "data": {
                },
                "message": "An error occurred adding the learner quiz."
            }
        ), 500

    return jsonify(
        {
            "code": 200,
            "message": "Learner Quiz has been added."
        }
    ), 201


if __name__ == '__main__':
    app.run(port=5010, debug=True)