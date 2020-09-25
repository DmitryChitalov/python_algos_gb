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


word = input('Введите строку: ')
set_obj = set()

for i in range(len(word) + 1):
    if i == 0:
        for j in range(len(word) - 1, i, -1):
            print(word[i:j])
            set_obj.add(hashlib.sha256(word[i:j].encode('utf-8')).hexdigest())
    for j in range(len(word), i, -1):
        print(word[i:j])
        set_obj.add(hashlib.sha256(word[i:j].encode('utf-8')).hexdigest())
print(f'Количество различных подстрок с использованием хеш-функции : {len(set_obj)}')
