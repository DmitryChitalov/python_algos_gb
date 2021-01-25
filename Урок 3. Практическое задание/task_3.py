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

user_input = input('Введите строку из маленьких букв:')
hash_lib = []
str_lenght = len(user_input)

for x in range(0, str_lenght + 1):
    for i in range(x + 1, str_lenght + 1):
        hash_lib.append(hashlib.sha256(user_input[x:i].encode('utf-8')).hexdigest())

hash_lib.remove(hashlib.sha256(user_input.encode('utf-8')).hexdigest())

print(f'Колличество подстрок в строке {user_input} ровно {len(set(hash_lib))}')