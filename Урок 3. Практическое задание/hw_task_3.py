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


def len_hash(str_, res=None):
    if res is None:
        res = set()
    length = len(str_)
    for i in range(length):
        if i == 0:
            length = len(str_) - 1
        else:
            length = len(str_)
        for j in range(length, i, -1):
            res.add(hashlib.sha256(str_[i:j].encode('utf-8')).hexdigest())
    print(res)
    print(f'Количество уникальных подстрок в строке "{str_}" равно: {len(res)}')


u_string = input('Введите cлово только из строчных латинских букв: ')
len_hash(u_string)
