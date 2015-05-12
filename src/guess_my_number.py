#!/usr/bin/env python3
# coding: utf-8
import random

print("Я загадал целое натуральное число от 1 до 100")

the_number = random.randint(1,100)
try:
    guess = int(input("Предположение: "))
except:
    print("Вводиблять числа! принято значение - 0")
    guess = int(0)
tries = 1
while guess != the_number:
    if guess > the_number:
        print("Меньше...",the_number)
        #print("Меньше...",the_number) # дебаг
    else:
        print("Болььше...",the_number)
        #print("Болььше...",the_number) # дебаг
    try:
        guess = int(input("Предположение: "))
        tries += 1
    except:
        print("Вводиблять числа! принято значение - 0")
        guess = int(0)
        tries += 1
print("Ура наконецто угодал и попыток было", tries)