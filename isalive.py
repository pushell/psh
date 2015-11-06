#!/usr/bin/env python3.4
# coding:utf-8

# Author:Yangmc
# Histroy:-2015.07.26
# Python:3.4.3
# Os:fedora 21&Centos 7
# Kernel:4.0.6-200.fc21.x86_64
# Version:0.1

"""
定义: 类IsAlive() ，方法：ping()  接受参数(IP) 
用于：SSH连接前，用ping检测主机存活状态.不输出信息.
      regex.findall() 对返回数据进行分析.找到 _seq 进行统计.
      大于0,则return self.ip+"up". 反之,则 return self.ip+"down"
注意: ping()方法会对self.ip进行重写.所以，对类 IsAlive()
      和方法ping()都要同时传入参数。

"""

import os
import re
import sys
import subprocess

class IsAlive():
    def __init__(self,ip="127.0.0.1"):
        self.ip=ip
        # print (self.ip)
    def ping(self,ipaddress="127.0.0.1"):
        self.ip=ipaddress
        result=subprocess.Popen(["ping -c 1 " + self.ip],stdout=subprocess.PIPE,shell=True)
        out = result.stdout.read()
        outf = out.decode("UTF-8")
        # print (outf)
        regex = re.compile("_seq",re.IGNORECASE | re.MULTILINE)
        if len(regex.findall(outf)) > 0:
            flag=self.ip +"up"
            # print (flag)
            return flag
        else:
            flag=self.ip+"down"
            # print (flag)
            return flag

if __name__ =='__main__':
    if len(sys.argv) < 2:
        print ("like this ./isalive 192.168.1.1 4")
    else:
        ip=sys.argv[1]
        p=IsAlive(ip)
        p.ping(ip)
