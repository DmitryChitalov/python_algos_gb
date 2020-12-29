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


def str_check_set(raw_str=input('Введите строку: '), result=set(), res_hash=set()):
    n = len(raw_str)
    for i in range(n):
        if i == 0:
            result.add(raw_str[i])
            result.add(raw_str[:i:-1])
        elif i == n-1:
            result.add(raw_str[:i])
        else:
            result.add(raw_str[:i])
            result.add(raw_str[:i:-1])
    [res_hash.add(sha256(j.encode('utf-8')).hexdigest()) for j in result]
    print(f'Количество подстрок в строке "{raw_str}" - {len(res_hash)} и они:')
    return [print(i) for i in sorted(result)]


str_check_set()
