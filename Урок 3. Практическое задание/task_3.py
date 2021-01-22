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

string_to_be_split = input('Please, insert the string for checking: ')
my_lst = []
for i in range(0, len(string_to_be_split) + 1):
    for k in range(i + 1, len(string_to_be_split) + 1):
        my_lst.append(hashlib.sha256(string_to_be_split[i:k].encode('utf-8')).hexdigest())

my_lst.remove(hashlib.sha256(string_to_be_split.encode('utf-8')).hexdigest())

print(f'The quantity of various substrings in the string {string_to_be_split} is {len(set(my_lst))}')

