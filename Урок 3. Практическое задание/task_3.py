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

def number_substrings(s, n, i):
    d1 = set()
    while n > 1:
        d1.add(hashlib.sha1(s[:n - 1].encode('utf-8')).hexdigest())
        d1.add(hashlib.sha1(s[i:].encode('utf-8')).hexdigest())
        i += 1
        n -= 1
    return f'Хеши подстрок: {d1}, \n' \
           f'количество элементов: {len(d1)}'

print(number_substrings('papa', 4, 1))






