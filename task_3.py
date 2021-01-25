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

def unique(lst='papa'):
    st_hash = set()
    st = set()
    for i in range(len(lst)):
        count = 1
        while count != len(lst):
            for n in lst:
                st.add(lst[i: i +count])
                st_hash.add(hashlib.sha256(lst[i: i + count].encode()).hexdigest())
            count += 1
    return st, st_hash
print(unique())



