from flask import Blueprint, Response, request
from services.WebCamService import WebCam
import cv2

REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API


def gen(webcam):
    capture = cv2.VideoCapture(0)
    if not capture:
        raise Exception("Error accessing the WebCam")

    while True:
        frame = webcam.get_frame(capture)
        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'
        )


@REQUEST_API.route('/stream')
def monitoring():
    try:
        webcam = WebCam()
        return Response(gen(webcam), mimetype='multipart/x-mixed-replace; boundary=frame')
    except Exception as err:
        return Response(f'Error {err}')
