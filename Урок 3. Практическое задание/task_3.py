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


def my_func(val, my_set=set()):
    for i in range(0, len(val) + 1):
        for j in range(i + 1, len(val) + 1):
            my_set.add(hashlib.sha256(val[i:j].encode('utf-8')).hexdigest())
    my_set.remove(hashlib.sha256(val.encode('utf-8')).hexdigest())
    return f'Количество разных подстрок: {len(my_set)}'


print(my_func(input('Введите строку: ')))