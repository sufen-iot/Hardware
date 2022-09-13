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

def get_hardware_info():
    #result = os.system('archey')
    
    info = { #example
        "cpu": "Raspberry Pi 3 Model B",
        "ram": "1 GB / test",
        "os": "Raspbian GNU/Linux 10 (buster)",
        "kernel": "Linux 4.19.97-v7+",
        "uptime": "1 day, 1 hour, 1 minute",
    }
    
    json_data = json.loads(info)
    
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    requests.post(hardware_url, data=json_data, headers=headers)

def get_sensor_info():
    
    requests.post()
    
def get_camera():
    #camera.capture('image.png')


    
    



