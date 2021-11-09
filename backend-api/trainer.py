import os
from os import error
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from mysql import connector
from dbModel import *
import decouple
from decouple import config

db_url=config("DB_URL")
db_password = config("DB_PASSWORD")

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:' + db_password + db_url
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)


# get the list of all trainers
@app.route("/trainer")
def get_all():
    trainer_list = Trainer.query.all()
    if len(trainer_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "trainers": [trainer.json() for trainer in trainer_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no trainers."
        }
    ), 404


# get specific trainer
@app.route("/trainer/<string:staffID>")
def get_trainer(staffID):
    trainer = Trainer.query.filter_by(staffID=staffID).first()
    if trainer:
        return jsonify(
            {
                "code": 200,
                "data": trainer.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Trainer not found."
        }
    ), 404


# add new trainer
@app.route("/trainer", methods=['POST'])
def add_trainer():


    staffID = request.json.get("staffID")
    numberOfClasses = request.json.get("numberOfClasses")

    trainer = Trainer(staffID=staffID, numberOfClasses=numberOfClasses)

    print(trainer.json())

    try:
        db.session.add(trainer)
        db.session.commit()
    except error:
        return jsonify(
            {
                "code": 500,
                "data": {
                },
                "message": "An error occurred adding the trainer."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": trainer.json()
        }
    ), 201


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5001, debug=True)
    app.run(host='0.0.0.0', port=5006, debug=True)
