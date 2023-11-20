#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# подсчитайте количество гласных в строке, введенной с клавиатуры с использованием множеств. 

if __name__ == "__main__":
    string_1 = set(input("Введите строку 1: "))
    string_2 = set(input("Введите строку 2: "))

    identical_characters = string_1.intersection(string_2)

    print(identical_characters)




