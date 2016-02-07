#!/usr/bin/env python3
# coding: utf-8

import subprocess
import re

CURL = "/usr/bin/curl"
ADDR = "http://95.167.19.218/stub_status"
nginx_stub = str(subprocess.check_output([CURL, "--silent", ADDR]))
output = re.findall('(\d+)', nginx_stub)

print(output[0])
print(output[4])
print(output[5])
print(output[6])
