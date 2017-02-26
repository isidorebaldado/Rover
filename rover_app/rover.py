import time
from itertools import cycle
from flask import Flask, render_template

import RPi.GPIO as GPIO

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"

@app.route("/forward")
def forward():
    return "Moving forward"

@app.route("/stop")
def stop():
    return "Moving backward"

@app.route("/stream")
def stream():
    return "Streaming video"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5010)
