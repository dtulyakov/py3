#!/usr/bin/env python3
# coding: utf-8

word = "пицца"
print(
"""
Памятка
0   1   2   3   4   5
+---+---+---+---+---+
| п | и | ц | ц | а |
+---+---+---+---+---+
-5  -4  -3  -2  -1
"""
)
print("Введите начальный и конечный индексы для того среза 'пиццы', который хотите получить")
start = None
while start !=" ":
    #start = str(input("Начальная позиция: "))
    start = int(input("Начальная позиция: "))
    if start:
        start = int(start)
        finish = int(input("Конецная позиция: "))
        print("Срез word[", start, ":", finish, "] выглядит как", end=" ")
        print(word[start:finish])
#if password == "secret":
#    print("Ok")
#    print("Пароле совпало")
#else:
#    print("Хера а не вход")
#try:
#    weight = int(input("введи вес: "))
#except:
#    print("Вводиблять числа")
#    weight = int(10)
#print("На луне вес был бы", weight / 6)
#print("На солнце вес был бы", weight * 27.1)
