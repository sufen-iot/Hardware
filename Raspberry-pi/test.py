import os
import math

MemTotal = os.popen("grep ^'MemTotal' /proc/meminfo").read()
MemFree = os.popen("grep ^'MemFree' /proc/meminfo").read()

MemTotal = MemTotal.replace("MemTotal:","").replace('kB','').replace(" ",'')
MemTotal =  int(MemTotal) / float(1000000)
print(MemTotal)

MemFree = MemFree.replace("MemFree:","").replace('kB','').replace(' ','')
MemFree = int(MemFree) / float(1000000)
print("{}GB / {}GB".format(round(MemTotal,1), round(round(MemTotal,4) - round(MemFree,4), 2)))