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
from hashlib import sha256


def str_func(n, m_set=None):
    if m_set is None:
        m_set = set()
    for i in range(len(n)):
        for j in range(len(n) - 1 if i == 0 else len(n), i, -1):
            m_set.add(sha256((n[i:j]).encode()).hexdigest())
    print(f'Количество подстрок в строке: {len(m_set)}')


str_func(n=input('Введите строку: '))