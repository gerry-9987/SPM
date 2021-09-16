import flask 
import time

app = flask.Flask(__name__)


@app.route("/")
def index():
    print("test! pls found")
    return "Welcome!!! ", time.localtime
