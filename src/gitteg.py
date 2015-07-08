#!/usr/bin/env python3
# coding: utf-8

from datetime import datetime, date, time
import subprocess
#print(datetime.today())

tagnum = datetime.today()
print("v"+tagnum.strftime("%Y%m%d"))
output = subprocess.check_output(["git", "tag"])
print(output)