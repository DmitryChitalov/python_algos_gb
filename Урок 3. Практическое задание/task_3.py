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
from uuid import uuid4

salt = uuid4().hex


def hash_create(str):
    hash_obj = hashlib.sha256(salt.encode() + str.encode()).hexdigest()
    return hash_obj


str = 'рара'
data = []
hashes = []

for i in range(len(str)):
    for j in range(i + 1, len(str) + 1):
        st = str[i:j]
        res = hash_create(st)
        if res not in hashes:
            data.append(st)
            hashes.append(res)

print(*zip(data, hashes))
