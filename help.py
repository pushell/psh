#!/usr/bin/env python3.4
# coding:utf-8

# Author:Yangmc
# Histroy:-2015.07.26
# Python:3.4.3
# Os:fedora 21&Centos 7
# Kernel:4.0.6-200.fc21.x86_64
# Version:0.1


cmd = {
     "sysname" : "PSH Imagine Software",
     "version" : "PSH&Imagine Software Version 0.4, Release 20150819P01",
     "ver" : "PSH&Imagine Software Version 0.4, Release 20150819P01",
     "q" : "quit",
     "?" : "help",
     "shutdown" : "ifdown",
     "undo shut" : "ifup",
     "vive_ip" : "call_view_ip()",
     "set_ip" : "call_set_ip()",
     "undo" : "ifdown",
     "display this" : "ifconfig",
     "md5" : "call_md5()",
     "key" : "call_execpwd()",
     "add" :  "call_add_server()"
     }


help = {
     "k" : "Usage: key <cr>",
     "ke" : "Usage: key <cr>",
     "K" : "Usage: key <cr>",
     "KE" : "Usage: key <cr>",
     "rolename" : "sa,na,dba",
     "sys" : """
 Usage:   int <sys> <cr>
 Example: int sys
             """,
     "SYS" : "Usage: int <sys> <cr>",
     "ss"  : "Usage: int <ssh> <cr>",
     "ssh" : """
 Usage:   int <ssh> <cr>
 Example: int ssh   
             """,
     "SSH" : "Usage: int <ssh> <cr>",
     "int" : """ 
 Usage:   int <sys/ssh> <cr> 
 Example: int sys 
           """,
     "INT" : "Usage: int <sys/ssh> <cr>",
     "ping" : """
 Usage:   ping  <-c count> <destination ip address> <cr>
 Example: ping -c 5 192.168.1.1 
             """,
     "del" : "Usage: del <server alias> <cr>",
     "add" : "Usage: add <alias> <ip address> <port> <cr>",
     "ver" : "PSH&Imagine Software Version 0.4, Release 20150819P01"
     }
