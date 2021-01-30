"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

import hashlib


def all_substr(s):
    l = len(s)
    s = set([s[b:b + a] for a in range(1, l) for b in range(l + 1 - a)])
    for i in range(len(s)):
        print(hashlib.sha1(s.pop().encode('utf-8')).hexdigest())


print(all_substr('papa'))


# s = input('str: ')
# r = set()
#
# N = len(s)
# for i in range(N):
#     if i == 0:
#         N == len(s) - 1
#     else:
#         N = len(s)
#     for j in range(N, i, -1):
#         print(s[i:j])
#         r.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
#
# print(r)
