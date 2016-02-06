#!/usr/bin/env python3
# coding: utf-8

from datetime import datetime
import subprocess

date_iso = datetime.today()
tagv = ("v" + date_iso.strftime("%Y%m%d"))
output = subprocess.check_output(["git", "tag", tagv])
