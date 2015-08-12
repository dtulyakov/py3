#!/usr/bin/env python3
# coding: utf-8
'''
Типа перекодировщик вавок в мп3
'''
import glob
import subprocess
from datetime import datetime

date_iso = datetime.today()
path = ("/home/ttys/spy/" + date_iso.strftime("%Y/%m/%d"))
list_files = glob.glob(path + '*.wav')

for files in list_files:
    output = subprocess.check_output(["lame", files])
    output = subprocess.check_output(["rm", files])
#EOF