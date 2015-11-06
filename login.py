#!/usr/bin/env python3.4
# coding:utf-8

# Author:Yangmc
# Histroy:2015.08.06
# Python:3.4.3
# Os:fedora 21&Centos 7
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




def checklevel(local_user,local_password):
    l_user=local_user
    l_pwd=local_password
    ins=db(host=HOST,port=PORT,user=USER,password=PASSWORD,db=DB)
    conn=ins.isconnect()
    if conn == 'error':
        print ("exit now! ")
        exit(0)
    loginflag='flase'
    try:
        with conn.cursor() as cur:
            checkuser="select `user`,`level`,`online` from im_sys_privileges where `user`=%s"
            checkpwd="select `passwd` from im_sys_privileges where `user`=%s"
            res=cur.execute(checkuser,(l_user))
            if res != 0:
                loginflag='true'
                exres=cur.fetchone()
                level=exres[1]
                online=exres[2]
                if online == 1:
                    print ("Max login limit!")
                if loginflag == 'true' and online == 0:
                    cur.execute(key,(l_pwd))
                    t_key=cur.fetchone()
                    t_key=t_key[0]
                    cur.execute(checkpwd,(l_user))
                    r_pwd=cur.fetchone()
                    r_pwd=r_pwd[0]
            
                    if t_key == r_pwd:
                        # print ("auth ok")
                        return level
                        cur.close()
                        conn.close()
                    else:
                        # print ("password failed")
                        loginflag='pwderror'
                        return loginflag
                        cur.close()
                        conn.close()
                else:
                    loginflag='usererror'
                    return loginflag
            else:
                loginflag='usererror'
                # print (loginflag)
                return loginflag           
    except:
        print ("Error!login.checklevel:88,未知错误")
    finally:
        conn.close()
 


def index_login():
    import getpass 
    from logbuff import Logbuff as logbuff
    print ( """
*******************************************************************************
*                        Welcome to Psh&Imagine shell !                       *
*    Please Enter your username and password ! Press CTRL_C to abort !        *
*******************************************************************************
     """)
    time=0
    while  time < 3:
        user=input("User:")
        if user.strip() != " ":
            password=getpass.getpass("Password:")
            if password.strip() != " ":
                level=checklevel(user,password)
                if level == 'usererror' or level == 'pwderror':
                    print ("Authentication failure !")
                    time+=1
                    continue;
                 
                else:
                    print ("Welcome %s !  %s" %(user,datetime.datetime.now()))
                    l=logbuff(logname=user+TIME+".log",logger=user)
                    l.logbuff.info(user+ " login!")
                    ins=db(host=HOST,port=PORT,user=USER,password=PASSWORD,db=DB)
                    conn=ins.isconnect()
                    if conn == 'error':
                        print ("exit now! ")
                        exit(0)
    
                    try:
                        with conn.cursor() as cur:
                            update_online="update `im_sys_privileges` set `online`=1  where `user`=%s"
                            cur.execute(update_online,user)
                            cur.close()
                    except:
                        print ("ERROR!login:index_login:131")
                    finally:
                        conn.commit()
                        conn.close()        
                    return level,user
                    break;
            else:
                time+=1
                continue;
        else:
            time+=1
            continue;
 


