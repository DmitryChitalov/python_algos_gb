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

mystring = input('Введите строку, состоящую только из маленьких латинских букв: ')

sum_substring = set()

for i in range(len(mystring)):
    for j in range(len(mystring), i, -1):
        hash_str = hashlib.sha1(mystring[i:j].encode('utf-8')).hexdigest()
        sum_substring.add(hash_str)

print(f'{len(sum_substring) -1} различных подстрок в строке {mystring}')
