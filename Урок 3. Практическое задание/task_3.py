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


def substrings(s):
    n = set()
    for i in range(len(s) - 1):
        for j in range(1 + i, len(s) + 1):
            n.add(hashlib.sha256(s[j - i - 1:j].encode()).hexdigest())
    return n


if __name__ == '__main__':
    my_str = 'papa'

    print(f'Колличество подстрок: {len(substrings(my_str))}')