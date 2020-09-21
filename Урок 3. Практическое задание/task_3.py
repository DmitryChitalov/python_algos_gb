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


def str_func(n, m_list=None, m_dict=None):
    if m_dict is None:
        m_dict = {}
    if m_list is None:
        m_list = []
    for i in range(len(n)):
        for j in range(len(n) - 1 if i == 0 else len(n), i, -1):
            m_list.append(hashlib.sha512((n[i:j]).encode()).hexdigest())
            m_dict[n[i:j]] = hashlib.sha512((n[i:j]).encode()).hexdigest()
    print(m_dict)
    print(f'Количество подстрок в строке: {len(set(m_list))}')


str_func(n=input('Input word: '))