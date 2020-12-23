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
from hashlib import md5


def substr(inp):
    res = []
    for i in range(1, len(inp) + 1):
        for k in range(0, i):
            el = md5(inp[k:i].encode()).hexdigest()
            res.append(el)
    sub_set = set(res)
    print(f'Число подстрок в слове {inp} - {len(sub_set) - 1}')


substr('papa')
