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

def unique_substrings(s : str):
    unique_set = set()
    for i in range(len(s)):
        unique_set.add(hashlib.sha256(s[:i].encode()).hexdigest())
        unique_set.add(hashlib.sha256(s[-i:].encode()).hexdigest())
    return unique_set, len(unique_set)

print(unique_substrings("рара"))
"""Вместе с пустой подстрокой длина равняется 7 : (6+1)"""
