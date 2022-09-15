import base64
from picamera import *

camera = PiCamera()
camera.resolution = (600, 600)
camera.capture('/home/pi/image.png')

with open("/home/pi/image.png", "rb") as img_file:
    base64_string = base64.b64encode(img_file.read())
print(base64_string.decode('utf-8'))