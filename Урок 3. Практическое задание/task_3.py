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

inp_str = input('Введите строку из строчных латинских букв: ')
N = len(inp_str)

set_of_substr = set()

for i in range(1, N):
    for j in range(i + 1):
        print(set_of_substr)
        print(inp_str[j:j + N - i])
        set_of_substr.add(hashlib.md5(inp_str[j:j + N - i].encode('utf-8')).hexdigest())
        print(set_of_substr)

print(f'Число подстрок в строке {inp_str} составляет {len(set_of_substr)}')
