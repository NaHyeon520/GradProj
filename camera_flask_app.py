from flask import Flask, redirect, url_for, render_template, request, flash, Response
import cv2
import datetime
import time
import os
import sys
import numpy as np
from threading import Thread
from image_preprocess import *


global capture, rec_frame, grey, switch, neg, face, rec, out
capture = 0
grey = 0
switch = 1
# make shots directory to save pics
try:
    os.mkdir('./shots')
except OSError as error:
    pass


app = Flask(__name__, template_folder='./templates')


camera = cv2.VideoCapture(0)


def gen_frames():  # generate frame by frame from camera
    global out, capture, rec_frame
    while True:
        success, frame = camera.read()
        if success:
            if (grey):
                # make frame green
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if (capture):  # capture frame
                capture = 0
                now = datetime.datetime.now()
                p = os.path.sep.join(
                    ['shots', "shot_{}.png".format(str(now).replace(":", ''))])
                cv2.imwrite(p, frame)
                global result
                result = convert_to_text(p)
                print(result)

            try:
                ret, buffer = cv2.imencode('.jpg', cv2.flip(frame, 1))
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as e:
                pass

        else:
            pass


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/requests', methods=['POST', 'GET'])  # make responsable buttons
def tasks():
    global switch, camera
    if request.method == 'POST':
        if request.form.get('click') == 'Capture':
            global capture
            capture = 1
        elif request.form.get('grey') == 'Grey':
            global grey
            grey = not grey

        elif request.form.get('stop') == 'Stop/Start':  # stop or start the camera

            if (switch == 1):
                switch = 0
                camera.release()
                cv2.destroyAllWindows()

            else:
                camera = cv2.VideoCapture(0)
                switch = 1

    elif request.method == 'GET':
        return render_template('index.html')
        # return redirect(url_for('tasks'))
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run()

camera.release()
cv2.destroyAllWindows()
