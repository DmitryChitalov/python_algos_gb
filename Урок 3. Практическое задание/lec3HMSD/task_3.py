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

k = set()
khash = set()
word = "рара"

for i in range(len(word)):
    for j in range(i + 1, len(word) + 1):
        k.add(word[i:j])
        khash.add(hashlib.sha256(word[i:j].encode()).hexdigest())

print(k)
print("Всего подстрок: ", len(k), " (включая саму строку)")
print(khash)
