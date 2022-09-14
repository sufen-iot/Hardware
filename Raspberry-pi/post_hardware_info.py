import json
import time
import os
import requests
import parse
import hardware

hardware_url = "https://api.plebea.site/hardware"

def post_hardware_info():
    
    
    '''info = {
        'cpu': hardware.cpu_info(),
        'ram': hardware.ram_info(),
        'os': hardware.os_info(),
        'kernel': hardware.kernel_info(),
        'uptime': hardware.uptime_info()
    }'''
    
    info = {
        "cpu": "cpu",
        "ram": "ram",
        "os": "os",
        "kernel": "kernel",
        "uptime": "uptime"
    }
    
    json_data = json.loads(info)
    
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    requests.post(hardware_url, data=json_data, headers=headers)
    
while(1): #5 min loop
    post_hardware_info()
    time.sleep(300)