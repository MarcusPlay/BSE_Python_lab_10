#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# подсчитайте количество гласных в строке, введенной с клавиатуры с использованием множеств. 

if __name__ == "__main__":
    input_string = input("Введите строку: ").lower()

    set_volue = set("aeiouаеёиоуыэюя")

    count = sum(1 for i in input_string if i in set_volue)

    print("Колличество гласных в веденной строке:", count)


