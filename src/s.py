#!/usr/bin/env python3
# coding: utf-8

IPS = 254
d_name = "moduli.ru"
d_block = "195.151.31."
#d_name = str(input("Домен: "))
#d_block = str(input("ИП: "))

name = d_name.replace(' ','')
block = d_block.replace(' ','')

if name == "":
    name = str("example.org")
else:
    pass

if block == "":
    block = str("192.168.0.")
else:
    pass

for ip in range(IPS):
    resolv_ip = (block + str(ip))
    print("s" + str(ip), resolv_ip)
    #print(str(ip), "PTR", resolv_ip)

#for ip in range(IPS):
#    #resolv_ip = (block + str(ip))
#    resolv_ip = (str(ip) + " PTR")
#    resolv_name = ("s" + str(ip) + "." + name)
#    print(resolv_ip, resolv_name)
#EOF
