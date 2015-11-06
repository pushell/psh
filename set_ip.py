#!/usr/bin/env python3.4
# coding:utf-8
# Author:Yangmc
# Histroy:-2015.07.17-07.28
# Python:3.4.3
# Os:fedora 21&Centos 7 
# Kernel:4.0.6-200.fc21.x86_64
# Version:0.3





def call_set_ip():
    while True: 
        int_info = []
        int_name = input("Enter Nic:(em1/enp6s0):")
        int_nameif = "ifcfg-"+int_name
        int_dir = "/etc/sysconfig/network-scripts/"
        int_path = int_dir+int_nameif
        int_info.append("IPADDR="+input("(ipaddress:)"))
        int_info.append("PREFIX="+input("(prefix:)"))
        int_info.append("GATEWAY="+input("(gateway:)"))
        int_info.append("DNS1="+input("(DNS:)"))
        int_info.append("BOOTPROTO=static")
        int_info.append("TYPE=Ethertnet")
        int_info.append("ONBOOT=yes")
        int_info.append("NAME="+int_name)
        os.system("clear")
        print ("\n请确认你的配置文件:")
        for line in int_info:
            print (line)  
        print ("\n按[ s ]保存配置立即生效(press s ,copy config to running ),按[ r ]重新生成配置!,按其它键返回!")      
        n = input(":")
        if n.lower() == "r":
            flag=1
            continue
        elif n.lower() == "s":
            f=open(int_path,"r+")
            print ("\n正在写入配置，请稍等(save file,Please wait..)...")
            f.write("\n".join(int_info))
            f.write("\n")
            f.flush()
            f.close()
            flag=0
            print ("\n配置已成功保存到%s,请重启网卡或网络服务！" %int_path)
            break
        else:
            flag=0
            break
            exit(0)
			
def call_view_ip():   
    os.system("ifconfig -a |more")
    print ("(network interface file list )")
    os.system("ls -l  /etc/sysconfig/network-scripts |grep ifcfg")
    input("(press enter key to continue)！")
    if input("(press y set ip address)！：").lower() == "y":
        call_set_ip()
    else:
        main()