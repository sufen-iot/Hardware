import base64
import json
import requests
import os 
import time
import threading
from pyfirmata import Arduino, util
#import picamera

info_url  = "https://api.plebea.site/accident"
hardware_url = "https://api.plebea.site/hardware"
board = Arduino("/dev/ttyACM0")

#camera = picamera.PiCamera()
#camera.resolution = (1920, 1080)


def get_sensor_info():
    
    heading = 0
    latitude = 0.0
    longitude = 0.0
    base64_img = ""
        
    info = {
        "heading": heading,
        "latitude": latitude,
        "longitude": longitude,
        "img": base64_img
    }
    
    json_data = json.loads(info)
    
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    requests.post(hardware_url, data=json_data, headers=headers)
    
def get_camera():
    #camera.capture('image.png')
    print("hi")
    
while(1):
    a = input("Press enter to take a picture")
    if a == 1:
        get_sensor_info()
        get_camera()
    else:
        continue
