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

string = 'papa'
substrs = [string[i:j] for i in range(len(string))
            for j in range(i + 1, len(string) + 1)]

hash_set = set()
for substr in substrs:
    hash_set.add(hashlib.sha256(substr.encode()).hexdigest())

print(f'В строке "{string}" содержится {len(hash_set)-1} уникальных подстрок.')