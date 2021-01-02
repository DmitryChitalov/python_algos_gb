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


my_list = []
my_str = input('Введите строку из любого количества маленьких латинских букв: _')
for n in range(0, len(my_str) + 1):
    for w in range(n + 1, len(my_str) + 1):
        my_list.append(hashlib.sha256(my_str[n:w].encode('utf-8')).hexdigest())

my_list.remove(hashlib.sha256(my_str.encode('utf-8')).hexdigest())
final_list = set(my_list)
print(final_list)
print(f'В строку {my_str} входит {len(final_list)} подстрок')



