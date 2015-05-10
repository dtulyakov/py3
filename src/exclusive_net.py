#!/usr/bin/env python3
# coding: utf-8

print("\nТипа мегасекурная сеть")
security = 0
username = ""
while not username:
	username = str(input("Login: "))
password = ""
while not password:
	password = str(input("Вводи пароль: "))
	
if username == "ttys" and password == "secret":
	print("Здаровченко Дениска")
	security = 5
elif username == "билгейтс" and password == "мудак":
	print("ну здрасте козлина")
	security = 3
elif username == "root" and password == "root":
	print("О здрастуйтесь ;-)")
	security = 3
elif username == "guest" or password == "guest":
	print("в гостяшки")
	security = 1
else:
	print("Хера а не вход")
#try:
#    weight = int(input("введи вес: "))
#except:
#    print("Вводиблять числа")
