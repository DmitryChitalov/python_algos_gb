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

# Честно говоря, тут не уверн, что так надо было решить, но вроде получилось
import random


def substring_number_from_string(n):
    s = ''
    substring_set = set()
    for idx in range(n):
        symb = chr(random.randint(65, 90)).lower()
        s += symb

    print(s)
    for idx in range(len(s)):
        for k in range(len(s)-1 if idx == 0 else len(s), idx, -1):
            substring_set.add(hash(s[idx:k]))
            #print(S[idx:k])

    print(f'Количество разных подстрок в строке "{s}" равно: {len(substring_set)}')


substring_number_from_string(5)
