#!/usr/bin/env python3
# coding: utf-8

#quote = " Думаю, на мировом рынке можно будет продать штук пять компьютеров. "
#print("Исходная цитата:")
#print(quote)
#print("\nOнa же в верхнем регистре:")
#print(quote.upper())
#print("\nB нижнем регистре:")
#print(quote.lower())
#print("\nKaк заголовок:")
#print(quote.title())
#print("\nC ма-а-аленькой заменой:")
#print(quote.replace("штук пять", "пару лямов"))
#print("\nA вот опять исходная цитата:")
#print(quote.strip())

try:
    car = float(input("Тех обслуживание тачки: "))
    rent = float(input("Сьём квартиры: "))
    jet = float(input("Сьём самолёта: "))
except:
    print("Вводиблять числа")
    car = int(0)
    rent = int(0)
    jet = int(0)
mf = str(input("стринга: "))
print(mf)
total = float(car + rent + jet)
print("\nОбщая сумма:", total)
try:
    age = int(input("\nвведи возраст: "))
except:
    print("Вводиблять числа")
    age = int(0)
seconds = age * 365 * 24 * 60 * 60
print(seconds)
try:
    weight = int(input("введи вес: "))
except:
    print("Вводиблять числа")
    weight = int(10)
print("На луне вес был бы", weight / 6)
print("На солнце вес был бы", weight * 27.1)
