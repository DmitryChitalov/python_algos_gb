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

def calc_substr(str):
    __calc_set = set()
    for i in range(len(str)):
        __calc_set.add(hashlib.md5(str[:i].encode()))
        __calc_set.add(hashlib.md5(str[-i:].encode()))
    return len(__calc_set)

print(calc_substr("рараs"))
