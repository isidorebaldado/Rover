import time
from itertools import cycle
from flask import Flask, render_template

import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.OUT)
p = GPIO.PWM(23, 50)  # channel=12 frequency=50Hz
p.start(0)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/forward")
def forward():
    ledOn()
    return "Moving forward"

@app.route("/stop")
def stop():
    ledOff()
    return "Moving backward"

@app.route("/stream")
def stream():
    return "Streaming video"

def ledOn():
    #start = int(GPIO.input(23))
    for dc in range(start, 101, 5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)
        print(p.dutycycle)
    return None

def ledOff():
    start = int(GPIO.input(23))
    for dc in range(start, 0, -5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)
    return None


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5010)
