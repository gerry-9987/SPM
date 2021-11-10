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



# get the list of all staff
@app.route("/staff")
def get_all():
    staff_list = Staff.query.all()
    if len(staff_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "staff": [staff.json() for staff in staff_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no staff."
        }
    ), 404


# get specific staff
@app.route("/staff/<string:staffID>")
def get_staff(staffID):
    staff = Staff.query.filter_by(staffID=staffID).first()
    if staff:
        return jsonify(
            {
                "code": 200,
                "data": staff.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Staff not found."
        }
    ), 404


# add new staff
@app.route("/staff", methods=['POST'])
def add_staff():


    staffID = request.json.get("staffID")
    staffUsername = request.json.get("staffUsername")
    staffName = request.json.get("staffName")
    department = request.json.get("department")

    staff = Staff(staffID=staffID, staffUsername=staffUsername, staffName=staffName, department=department)

    print(staff.json())

    try:
        db.session.add(staff)
        db.session.commit()
    except error:
        return jsonify(
            {
                "code": 500,
                "data": {
                },
                "message": "An error occurred adding the staff."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": staff.json()
        }
    ), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
