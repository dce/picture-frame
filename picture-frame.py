import os
from flask import Flask, render_template

PICTURE_PATH = "/home/pi/picture-frame/pictures"

app = Flask(__name__)

@app.route("/")
def index():
    files = os.listdir(PICTURE_PATH)
    return render_template("index.html", files=files)
