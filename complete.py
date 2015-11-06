#!/usr/bin/env python3.4
# coding:utf-8

# Author:Yangmc
# Histroy:-2015.08.25
# Python:3.4.3
# Os:fedora 21&Centos 7
# Kernel:4.0.6-200.fc21.x86_64
# Version:0.1

import readline

cmd = [
      '?',
      'ver', 
      'int',
      'sys',
      'ssh',
      'add',
      'del',
      'key',
      'who',
      'conn',
      'list',
      'help',
      'rule',
      'allow',
      'access',
      'role',
      'push',
      'show',
      'pull',
      'time',
      'host',
      'group',
      'level',
      'passwd',
      'cipher',
      'current',
      'local-user',
      'quit'
       ]

def completer(text, state):
    options = [x for x in cmd if x.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")


