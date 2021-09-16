import flask, time

app = flask.Flask(__name__)


@app.route("/")
def index():
    print("test!")
    return "Welcome!!! ",time.localtime
