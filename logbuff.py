#!/usr/bin/env python3.4
# coding:utf-8

# Author:Yangmc
# Histroy:-2015.08-12
# Python:3.4.3
# Os:fedora 21&Centos 7
# Kernel:4.0.6-200.fc21.x86_64
# Version:0.1

import sys

import pshconf

sys.path.append(pshconf.runpath)
sys.path.append(pshconf.packsys)
sys.path.append(pshconf.packpymysql)

logpath=pshconf.logpath



class Logbuff():
    def __init__(self,logname,logger):
        '''
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        '''
        import logging
        logging.basicConfig(level=logging.INFO,
                format='%(asctime)s:(%(name)s):[%(levelname)s]: %(message)s',
                datefmt='%Y-%m-%d %H-%M-%S',
                filename=logpath+logname,
                filemode='a+')



        # 创建一个logbuff
        self.logbuff = logging.getLogger(logger)
        self.logbuff.setLevel(logging.INFO)

        # 创建一个handler，用于写入日志文件
        # log = logging.FileHandler(filename=logpath+logname,mode='a+',encoding='utf-8',delay=False)
        # log.setLevel(logging.INFO)
        # 定义handler的输出格式
        # formatter = logging.Formatter('%(asctime)s:%(name)s-[%(levelname)s]: %(message)s')
        # formatter = format_dict[int(loglevel)]
        # log.setFormatter(formatter)

        # 给logger添加handler
        # self.logbuff.addHandler(log)
        # log.flush()
       
   
    def getlog(self):
        return self.logbuff
