#!/usr/bin/env python3
# coding: utf-8

print("\nСимулятор ребёнка")
print("Попробуй остановить")
response = "небо синее"
while response != "Потому что":
	print("Почему", response.lower(), "?")
	response = str(input())
print("A, ладно")
