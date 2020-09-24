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


def substring_hashing(_string):
    result = set()
    _string = _string.lower()
    for el in range(len(_string)):
        for i in range(len(_string)):
            result.add(hashlib.sha256(_string[el:i].encode('utf-8')).hexdigest())
    return result


my_string = input('Напиши слово: ')
str_hash = substring_hashing(my_string)

print(f'Различных подстрок: {len(str_hash)}')
