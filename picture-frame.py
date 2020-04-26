import os
import glob

from flask import Flask, render_template
from papirus import PapirusImage

PICTURE_PATH = "/home/pi/picture-frame/pictures"

app = Flask(__name__)

@app.route("/")
def index():
    files = map(os.path.basename,
            glob.glob(os.path.join(PICTURE_PATH, "*.png")))
    return render_template("index.html", files=files)

@app.route("/<filename>")
def draw(filename):
    path = os.path.join(PICTURE_PATH, filename)

    if os.path.isfile(path):
        image = PapirusImage()
        image.write(path)
        return 'ok'

    else:
        return '404', 404
