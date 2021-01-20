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


def all_substr(s):
    l = len(s)
    return set([s[b:b + a] for a in range(1, l) for b in range(l + 1 - a)])


test_str = 'papa'
for sub in all_substr(test_str):
    print(sub)
