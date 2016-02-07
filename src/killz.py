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
import os
import subprocess
# import re

# z = subprocess.check_output(["w", "-hs"])
# z = os.system("w -sh")
z = os.system("./killz.sh")
# z = str(subprocess.check_output(["w", "-hs"]))
z2 = str(subprocess.check_output(["./killz.sh"]))
# z = z.split('')
# oz = re.findall('(\d+)', z)


def main():
    # subprocess.call(record + path + date_path + file_mp3, shell=True)
    print(z)
    print("========")
    print(z2)
    # print(z[1])
if __name__ == '__main__':
    main()
