#!/usr/bin/env python3
# coding: utf-8
import random

word = "индекс"
print("В переменной word хоанится слово:", word, "\n" )
high = len(word)
low = -len(word)
for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])