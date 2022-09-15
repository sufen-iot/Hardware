import base64
from picamera import *

camera = PiCamera()
camera.resolution = (600, 600)

def base64_encoding():
    with open("/home/pi/image.png", "rb") as img_file:
        base64_string = base64.b64encode(img_file.read())
    return base64_string.decode('utf-8')

def get_camera():
    camera.capture('/home/pi/image.png')

