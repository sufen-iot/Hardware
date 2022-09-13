import json
import requests
import os 
import time
import threading
from pyfirmata import Arduino, util

url  = "https://api.plebea.site/accident"
board = Arduino("/dev/ttyACM0")

def get_hardware_info():
    result = os.system('archey')
    
    info = { #example
        "cpu": "Raspberry Pi 3 Model B",
        "ram": "1 GB",
        "gpu": "Broadcom BCM2837",
        "os": "Raspbian GNU/Linux 10 (buster)",
        "kernel": "Linux 4.19.97-v7+",
        "uptime": "1 day, 1 hour, 1 minute",
        "shell": "bash 5.0.3",
        "resolution": "1920x1080",
        "de": "Raspberry Pi Configuration"
    }
    
    json_data = json.loads(result)
    
    requests.post()

def get_sensor_info():
    print("hi")

while(1): #5 min loop
    get_hardware_info()
    time.sleep(300)
    
    



