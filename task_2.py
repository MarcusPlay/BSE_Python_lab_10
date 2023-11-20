#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# определите общие символы в двух строках, введенных с клавиатуры. 


if __name__ == "__main__":
    string_1 = set(input("Введите строку 1: "))
    string_2 = set(input("Введите строку 2: "))

    identical_characters = string_1.intersection(string_2)

    print(identical_characters)




