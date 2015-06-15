#!/usr/bin/env python3
# coding: utf-8

message = str(input("Введите текст: "))
print("\nДлина введённого текста состовляет:", len(message))
print("Самая частая согласная, 'т',")
if "т" in message.lower():
    print("встречается в вашем тексте.") 
else:
    print("не встречается в вашем тексте.") 
