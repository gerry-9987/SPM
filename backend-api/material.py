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

if __name__ == '__main__':
    app.run(port=5009, debug=True)