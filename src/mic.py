#!/usr/bin/env python3
# coding: utf-8
'''
Можно было шандарахнуть и так но это не наш метод
import os
os.system(record + ("/home/ttys/frommic/" + date_iso.strftime("%Y/%m/%d/")) + (date_iso.strftime("%Y%m%d-%H") + ".mp3"))
os.system(record + path + date_path + file_mp3)

Почему не system?
Потому, что считается более правильным использовать subprocess
'''
import subprocess
from datetime import datetime
from distutils.dir_util import mkpath

date_iso = datetime.today()
date_path = (date_iso.strftime("%Y/%m/%d/"))
date_file = (date_iso.strftime("%Y%m%d-%H"))

path = "/home/ttys/mic/"
record = "arecord --buffer-time=5000000 -D plughw:0,0 -f S16_LE --use-strftime - | lame - >"
file_mp3 = date_file + ".mp3"

mkpath(path)
subprocess.call(record + path + date_path + file_mp3, shell=True)
#EOF