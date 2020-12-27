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


def substring_count(string):
    substrings = set()
    for i in range(len(string) + 1):
        for j in range(len(string) + 1):
            if i == 0:
                substrings.add(hashlib.sha256(string[i:-1].encode()).hexdigest())
            elif j >= i and i != 0 and string[i:j] != '':
                substrings.add(hashlib.sha256(string[i:j].encode()).hexdigest())
    return len(substrings)


print(substring_count('papa'))
