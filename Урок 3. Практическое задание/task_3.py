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


def check_substrings(lcl_str=''):
    lcl_set = set()
    for i in range(len(lcl_str)):
        for j in range(i + 1, len(lcl_str) + 1):
            if lcl_str[i:j] != lcl_str:
                lcl_set.add(hashlib.sha256(lcl_str[i:j].encode('utf-8')).hexdigest())
    return lcl_set


my_str = input('Ввдеите строку для проверки: ')
print(check_substrings(my_str))

