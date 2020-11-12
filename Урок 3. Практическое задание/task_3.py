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


s = input("Введите строку: ")
arr = set()

n = len(s)
for i in range(n):
    if i == 0:
        n = len(s) - 1
    else:
        n = len(s)
    for j in range(n, i, -1):
        arr.add(hashlib.sha256(s[i:j].encode()).hexdigest())

print('Количество подстрок: ', len(arr))