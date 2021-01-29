"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""

import hashlib

# some_string = "papa"
some_string = input("Введите строку: ")
dataset = set()

length = len(some_string)
for i in range(length):
    if i == 0:
        length == len(some_string) - 1
    else:
        N = len(some_string)
    for j in range(length, i, -1):
        print(some_string[i:j])
        dataset.add(hashlib.md5(some_string[i:j].encode('utf-8')).hexdigest())

print(f' Все хеши подстрок: {dataset}')
