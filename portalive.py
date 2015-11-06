#!/usr/bin/env python3.4
#coding:utf-8

# Author:Yangmc
# Histroy:-201507.27
# Python:3.4.3
# Os:fedora 21&Centos 7
# Kernel:4.0.6-200.fc21.x86_64
# Version:0.1


import os
import sys
import time
import socket

"""
定义: 方法 portalive(),接受参数(ip,port)
用于: SSH连接前，进行端口开启检测。
      设置sc.timeout(2)避免长时间等待
      连接成功 return "open" 反之，return "donw"

"""

def portalive(ip,port):
    sc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # ip=i.split(",")[0]
    # i=input("ip,port:")
    # port=i.split(",")[1]
    
    sc.settimeout(2)
    
    try:
        sc.connect((ip,int(port)))
        sc.close()
        timenow=time.localtime()
        datenow=time.strftime('%Y-%m-%d %H:%M:%S',timenow)
        logstr="%s:%s -->connection ok. %s" %(ip,port,datenow)
        # print (logstr)
        return "open"
    except:
        timenow=time.localtime()
        datenow=time.strftime("%Y-%m-%d %H:%M:%S",timenow)
        logstr="%s %s connection failed. %s" %(ip,port,datenow)
        # print (logstr)
        return "down"



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print ("[line this: ./portalive 192.168.1.1 80]")
    else:
        ip=sys.argv[1]
        port=sys.argv[2]
        portalive(ip,port) 
