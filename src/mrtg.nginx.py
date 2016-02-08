#!/usr/bin/env python3
# coding: utf-8
'''
Вытащить числа ещё можно регэкспом - но медленне
'''
# from datetime import datetime, date, time
import subprocess

CURL = "/usr/bin/curl"
ADDR = "http://95.167.19.218/stub_status"
# date_iso = datetime.today()
# tagv = ("v" + date_iso.strftime("%Y%m%d"))
nginx_stub = str(subprocess.check_output([CURL, "--silent", ADDR]))
output = [int(s) for s in nginx_stub.split() if s.isdigit()]

print(output[0])
print(output[4])
print(output[5])
print(output[6])
