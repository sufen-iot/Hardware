import os

#하드웨어 정보를 불러오는 자체 제작 파이썬 라이브러리 입니다.


def cpu_info(): #시스템 CPU 정보를 불러오는 함수입니다.
    cpu_info = os.popen("grep ^'model name' /proc/cpuinfo").read()
    cpu_info = cpu_info.replace('model name', '').split(':')
    
    return cpu_info[1]

def ram_info(): #현재 시스템 총 메모리와 현 메모리 사용량을 나타내는 함수입니다.
    MemTotal = os.popen("grep ^'MemTotal' /proc/meminfo").read()
    MemFree = os.popen("grep ^'MemFree' /proc/meminfo").read()

    MemTotal = MemTotal.replace("MemTotal:","").replace('kB','').replace(" ",'')
    MemTotal =  int(MemTotal) / float(1000000)

    MemFree = MemFree.replace("MemFree:","").replace('kB','').replace(' ','')
    MemFree = int(MemFree) / float(1000000)
    
    return "{}GB / {}GB".format(round(MemTotal,1), round(round(MemTotal,4) - round(MemFree,4), 2))
    
def os_info(): #시스템 OS 정보를 불러오는 함수입니다
    os_info = ""
    os_info = os.popen("grep ^'PRETTY_NAME' /etc/os-release").read()
    
    return os_info.replace("PRETTY_NAME=","").replace("'","")
    
def kernel_info(): #시스템 커널 정보를 불러오는 함수입니다.
    kernel_info = os.popen("uname -r").read()
    
    return kernel_info

def uptime_info(): #시스템 작동 시간을 불러오는 함수입니다.
    uptime_info = os.popen("uptime").read()
    uptime_info = uptime_info.split(",")
    
    return uptime_info[0]

