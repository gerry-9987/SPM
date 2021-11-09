from os import error
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from dbModel import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:' + db_password + '@spm-g8t9-db.cdlmqct6kw9s.us-east-1.rds.amazonaws.com:3306/spm_proj'

# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)


# get the list of all learners
@app.route("/learner")
def get_all():
    learner_list = Learner.query.all()
    if len(learner_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learners": [learner.json() for learner in learner_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no learners."
        }
    ), 404


# get specific learner
@app.route("/learner/<string:staffID>")
def get_learner(staffID):
    learner = Learner.query.filter_by(staffID=staffID).first()
    if learner:
        return jsonify(
            {
                "code": 200,
                "data": learner.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Learner not found."
        }
    ), 404


# add new learner
@app.route("/learner", methods=['POST'])
def add_learner():


    staffID = request.json.get("staffID")
    numberOfClassesPassed = request.json.get("numberOfClassesPassed")

    learner = Learner(staffID=staffID, numberOfClassesPassed=numberOfClassesPassed)

    print(learner.json())

    try:
        db.session.add(learner)
        db.session.commit()
    except error:
        return jsonify(
            {
                "code": 500,
                "data": {
                },
                "message": "An error occurred adding the learner."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": learner.json()
        }
    ), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
