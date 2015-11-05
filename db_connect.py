#!/usr/bin/env python3.4
# coding:utf-8

# Author:Yangmc
# Histroy:2015.08.05
# Python:3.4.3
# Os:fedora 21&Centos 7
# Kernel:4.0.6-200.fc21.x86_64
# Version:0.1


import os
import sys
import configparser

import pymysql
import pshconf

class Db_Connect():
    def __init__(self,host='localhost',port=3306,user='root',password=' ',db='mysql'):
        self.host=host
        self.port=port
        self.dbuser=user
        self.dbpassword=password
        self.db=db
    def isconnect(self):
        try:
            self.conn = pymysql.connect(host=self.host,port=self.port,user=self.dbuser,password=self.dbpassword,db=self.db)
            return self.conn
        except:
            print ("connect database error,check config pshconf.py or you must run ./db_init.py ")
            return 'error'   
         
    def db_init():
        config=configparser.ConfigParser()
        conf=config.read(pshconf.imagineconf)
        ins=Db_Connect(host=config.get('db','host'),port=config.getint('db','port'),user=config.get('db','user'),password=config.get('db','password'),db=config.get('db','db'))
        conn=ins.isconnect()
        if conn == 'error':
            print ("connect database error!")
            exit(0)
        try:
            with conn.cursor() as cur:
                create_db="CREATE DATABASE `psh_imagine` DEFAULT CHARACTER SET utf8"
                create_table="CREATE TABLE `psh_imagine`.`im_sys_privileges` (`id` int(11) NOT NULL AUTO_INCREMENT, `user` varchar(60) NOT NULL, `passwd` varchar(255) NOT NULL,`level` int(11) NOT NULL,`regtime` datetime NOT NULL,`full_name` varchar(255) DEFAULT NULL,`sa` varchar(30) NOT NULL,`na` varchar(30) NOT NULL,`dba` varchar(30) NOT NULL,`online` int(11) NOT NULL, PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 "
                insert_data="insert into `psh_imagine`.`im_sys_privileges` values ('','admin',md5(password('admin')),3,now(),'admin',1,1,1,0)"
                if cur.execute(create_db):
                    print ("create db ok! 创建库，成功!")
                res_create_table=cur.execute(create_table) 
                res_insert_data=cur.execute(insert_data)
                if res_insert_data == 1:
                    print ("initialization ok! 初始数据，成功!")   
        except:
            print ("initialization  failure!初始化失败")
        finally:
            conn.commit()
            conn.close()

if  __name__  == '__main__':
    if sys.argv[1] == 'init':
        Db_Connect.db_init()
    else:
        pass

