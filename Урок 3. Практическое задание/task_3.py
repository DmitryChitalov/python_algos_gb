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

stroka = input('Введите строку: ')
a = set()
for i in range(len(stroka) - 1):
    a.add(hashlib.sha1(stroka[i + 1:].encode('utf-8')).hexdigest())
    a.add(hashlib.sha1(stroka[:len(stroka) - i - 1].encode('utf-8')).hexdigest())
print(a)
