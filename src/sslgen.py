#!/usr/bin/env python3
# coding: utf-8

d_name = str(input("Имя домена: "))
name = d_name.replace(' ','')
if name == "":
    name = str("example.org")
else:
    pass

for file in "dev.", \
    "alpha.", \
    "release.", \
    "beta.", \
    "ftp.", \
    "pop.", \
    "imap.", \
    "ssl.", \
    "test.", \
    "python.", \
    "sphinx.", \
    "django.", \
    "java.", \
    "spring.", \
    "hibernate.", \
    "js.", \
    "perl.", \
    "ruby.",\
    "rails.", \
    "jenkins.", \
    "qwerty.", \
    "u.", \
    "d.", \
    "db.", \
    "tengine.", \
    "nginx.", \
    "t.", \
    "gf.", \
    "at.", \
    "spring.":
    print(file+name.lower())
#EOF
