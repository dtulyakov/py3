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

z = subprocess.check_output(["w"])


def main():
    # subprocess.call(record + path + date_path + file_mp3, shell=True)
    print(z)
if __name__ == '__main__':
    main()
