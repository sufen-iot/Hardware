import json
import time
import os 
import requests
import hardware #자체제작 라이브러리

hardware_url = "https://api.plebea.site/hardware" #백엔드 api 주소

def post_hardware_info(): 
    #하드웨어 정보 제공 라이브러리를 이용하여 정보를 받아온 후 json으로 가공하여 api 서버에 post로 보냅니다

    info = { #json으로 가공하기 위한 딕셔너리 생성
        'cpu': hardware.cpu_info(),
        'ram': hardware.ram_info(),
        'os': hardware.os_info(),
        'kernel': hardware.kernel_info(),
        'uptime': hardware.uptime_info()
    }
    
    json_data =json.dumps(info, indent=2) #json 데이터로 가공
    
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    requests.post(hardware_url, data=json_data, headers=headers) #post로 전송
    
while(1): #5분 간격으로 하드웨어 정보 전송
    post_hardware_info()
    time.sleep(300)
