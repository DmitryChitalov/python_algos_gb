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


SALT = 'Hello World'

def check_str(string):
    answer = set()
    n = len(string)
    for s in range(1, n, 1):
        for i in range(n-s+1):
            res = hashlib.sha256(SALT.encode() + string[i:(i+s)].encode()).hexdigest()
            answer.add(res)
    return f'В строке "{string}" - всего подстрок {len(answer)}'


print(check_str('papa'))
