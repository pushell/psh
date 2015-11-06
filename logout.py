#!/usr/bin/env python3.4
# coding:utf-8

# Author:Yangmc
# Histroy:2015.08.26
# Python:3.4.3
# Os:fedora 21&& Centos 7&& debian 8.1 && openSUSE 13.2
# Kernel:4.0.6-200.fc21.x86_64
# Version:0.1


import os
import sys
import time
import datetime
import configparser

import pshconf
sys.path.append(pshconf.runpath)
sys.path.append(pshconf.packsys)
sys.path.append(pshconf.packpymysql)

import pymysql
from db_connect import Db_Connect as db


key="select md5(password(%s))"
config=configparser.ConfigParser()
conf=config.read(pshconf.imagineconf)
DB=config.get('db','db')
HOST=config.get('db','host')
USER=config.get('db','user')
PORT=config.getint('db','port')
PASSWORD=config.get('db','password')
TIME=str(time.localtime()[0])+str(time.localtime()[1])+str(time.localtime()[2])



def logout(local_user):
    l_user=local_user
    ins=db(host=HOST,port=PORT,user=USER,password=PASSWORD,db=DB)
    conn=ins.isconnect()
    if conn == 'error':
        print ("exit now! ")
        exit(0)
    try:
        with conn.cursor() as cur:
            logout_online="update im_sys_privileges set `online`=0  where `user`=%s"
            if cur.execute(logout_online,(l_user)):
                cur.close()
                return 'ok'           
    except:
        print ("Error!login.checklevel:88,未知错误")
    finally:
        conn.commit()
        conn.close()
 


 


