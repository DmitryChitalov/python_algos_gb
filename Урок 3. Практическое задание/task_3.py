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


def pgm(str: str):
    unique_set = set()
    for i in range(len(str)):
        unique_set.add(hash(str[:i]))
        unique_set.add(hash(str[-i:]))
    return len(unique_set) - 1


print(pgm("papa"))
