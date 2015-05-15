#!/usr/bin/env python3
# coding: utf-8

print("\nПосчитаем")
for i in range(10):
    print(i, end=" ")
print("\n\nПеречислим кратные пяти:")
for i in range(0, 50, 5):
    print(i, end=" ")
print("\nПересчитаем в обратном порядке")
for i in range(10, 0, -1):
    print(i, end=" ")

#try:
#    weight = int(input("введи вес: "))
#except:
#    print("Вводиблять числа")
#    weight = int(10)
#print("На луне вес был бы", weight / 6)
#print("На солнце вес был бы", weight * 27.1)
