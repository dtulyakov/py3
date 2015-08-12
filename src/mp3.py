#!/usr/bin/env python3
# coding: utf-8
'''
Типа граббер
'''
import os
import subprocess
from datetime import datetime, date, time
#from lxml import etree

date_iso = datetime.today()
path = ("/home/ttys/spy/" + date_iso.strftime("%Y/%m/%d"))
path="/home/ttys/spy/2015/07/20/"
list_files = os.listdir(path)

for files in list_files:
    if files.endswith('.wav'):
        #output = subprocess.check_output(["lame", path + files])
        print(path + files)
#EOF
