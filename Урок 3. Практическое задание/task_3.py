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

s = str(input("Введите строку: "))

subs_set = set()

for i in range(len(s)):
    for j in range(len(s) - 1 if i == 0 else len(s), i, -1):
        subs_set.add(hashlib.sha256(s[i:j].encode()).hexdigest())

print("Количество различных подстрок в этой строке:", len(subs_set))
