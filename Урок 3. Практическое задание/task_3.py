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

my_string = input('Введите новую строку: ')

subs = set()

for i in range(len(my_string)):
    for j in range(len(my_string) - 1 if i == 0 else len(my_string), i, -1):
        subs.add(hashlib.sha1(my_string[i:j].encode('utf-8')))
        print(my_string[i:j])

print("Количество различных подстрок в этой строке:", len(subs))
