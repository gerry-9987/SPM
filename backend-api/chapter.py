from os import error
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/spm_proj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Chapter(db.Model):


    __tablename__ = 'chapter'
    chapterID = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    chapterName = db.Column(db.VARCHAR(255), nullable=False)
    quizID = db.Column(db.Integer(), db.ForeignKey('quiz.quizID'), nullable=False)


    def __init__(self, chapterID, chapterName, quizID):
        self.chapterID = chapterID
        self.chapterName = chapterName
        self.quizID = quizID


    def json(self):
        return {
            "chapterID": self.chapterID,
            "chapterName": self.chapterName,
            "quizID": self.quizID,
        }


# get the list of all chapters
@app.route("/chapter")
def get_all_chapters():
    chapter_list = Chapter.query.all()
    if len(chapter_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "chapters": [chapter.json() for chapter in chapter_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no chapters."
        }
    ), 404


# get specific chapter
@app.route("/chapter/<string:chapterID>")
def get_chapter(chapterID):
    chapter = Chapter.query.filter_by(chapterID=chapterID).first()
    if chapter:
        return jsonify(
            {
                "code": 200,
                "data": chapter.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Chapter not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)
