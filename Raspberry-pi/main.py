import json
import requests
import os 
import time
import sensor


info_url  = "https://api.plebea.site/accident"


heading = 0
latitude = 0.0
longitude = 0.0
base64_img = ""


def post_sensor_info():
            
    info = {
        "heading": heading,
        "latitude": latitude,
        "longitude": longitude,
        "img": sensor.base64_encoding()
    }
    
    json_data = json.dumps(info, indent=2)
    
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    requests.post(info_url, data=json_data, headers=headers)
    

    
sensor.get_camera()
post_sensor_info()
