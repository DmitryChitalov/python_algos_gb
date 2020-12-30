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
        __sub1 = str[:i].encode()
        __sub2 = str[-i:].encode()
        if __sub1:
            __calc_set.add(hashlib.md5(__sub1).hexdigest())
        if __sub2:
            __calc_set.add(hashlib.md5(__sub2).hexdigest())
    return len(__calc_set)

print(calc_substr("рараs"))
