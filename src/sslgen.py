#!/usr/bin/env python3
# coding: utf-8
'''
Имя файла sslgen.py - первое что пришло в голову
Генератор сабдоменов при регистрации халявных ссл сертификатов
name = ' '.join(name.split()) создаёт список или я чёто не так делаю ...
'''
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
    "spring." \
    "blog.", \
    "wiki.":
    print(file+name.lower())
#EOF
