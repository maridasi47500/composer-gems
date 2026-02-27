from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>&#127470;&#127481;italian music</p><p>music de france&#127467;&#127479;</p><p>musique allemande&#127465;&#127466;</p><p>musique russe &#127479;&#127482;</p>"
