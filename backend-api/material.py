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

@app.route("/material")
def get_all():
    material_list = Material.query.all()
    if len(material_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "material": [material.json() for material in material_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no materials."
        }
    ), 404


@app.route("/material/<string:chapterID>")
def get_material_details(chapterID):

    materials = Material.query.filter_by(chapterID=chapterID).all()
    if len(materials) > 0:
        materialDetails = [
            {
                "materialID": material.materialID,
                "materialName": material.materialName,
                "materialType": material.materialType,
                "materialLink": material.materialLink,
                "materialLinkBody": material.materialLinkBody,
                "chapterID": material.chapterID,
                "classID": material.classID,
                "courseID": material.courseID
            }
            for material in materials]

        return jsonify(
            {
                "code": 200,
                "data": materialDetails
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Materials not found."
        }
    ), 404

# add new material
@app.route("/material", methods=['POST'])
def create_material():

    materialID = request.json.get("materialID")
    materialName = request.json.get("materialName")
    materialType = request.json.get("materialType")
    materialLink = request.json.get("materialLink")
    materialLinkBody = request.json.get("materialLinkBody")
    chapterID = request.json.get("chapterID")
    classID = request.json.get("classID")
    courseID = request.json.get("courseID")

    material = Material(
        materialID=materialID,
        materialName=materialName,
        materialType=materialType,
        materialLink=materialLink,
        materialLinkBody=materialLinkBody,
        chapterID=chapterID,
        classID=classID,
        courseID= courseID
    )
    findmaterial = Material.query.filter(Material.materialID==materialID).first()

    if not findmaterial:
        db.session.add(material)
        db.session.commit()
        return jsonify(
            {
                "code": 201,
                "data": material.json()
            }
        ), 201
    else:
        return jsonify(
            {
                "code": 500,
                "message": "Material already exists."
            }
        ), 500


# add new material
@app.route("/material", methods=['PUT'])
def update_material():

    materialID = request.json.get("materialID")
    materialName = request.json.get("materialName")
    materialType = request.json.get("materialType")
    materialLink = request.json.get("materialLink")
    materialLinkBody = request.json.get("materialLinkBody")
    chapterID = request.json.get("chapterID")
    classID = request.json.get("classID")
    courseID = request.json.get("courseID")

    material = Material.query.filter(
        Material.materialID==materialID,
        Material.chapterID==chapterID,
        Material.classID==classID,
        Material.courseID==courseID
    ).first()

    if material:
        material.materialName = materialName
        material.materialType = materialType
        material.materialLink = materialLink
        material.materialLinkBody = materialLinkBody
        material.chapterID = chapterID
        material.classID = classID
        material.courseID = courseID

        material.save_to_db()
        return jsonify(
            {
                "code": 200,
                "data": material.json()
            }
        ), 200
    else:
        return jsonify(
            {
                "code": 500,
                "message": "Material does not exist yet."
            }
        ), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)