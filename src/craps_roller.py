#!/usr/bin/env python3
# coding: utf-8
import random

die1 = random.randint(1,6)
die2 = random.randrange(6) + 1
total = die1 + die2
print("Первый кубик", die1, "второй кубик", die2, "Сумма", total)
#try:
#    weight = int(input("введи вес: "))
#except:
#    print("Вводиблять числа")
#    weight = int(10)
#print("На луне вес был бы", weight / 6)
#print("На солнце вес был бы", weight * 27.1)
