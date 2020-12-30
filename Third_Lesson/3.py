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
        unique_set.add(s[:i + 1]) # Здесь накосячил, т.к при срезе [0:0] возвращалась пустая строка ибыл 7 элементов, а не 6
        unique_set.add(s[-i:])
    return unique_set, len(unique_set)

print(unique_substrings("рара"))

