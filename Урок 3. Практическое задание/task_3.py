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


def hash_set(string):
    result = set()
    for i in range(len(string), -1, -1):

        for k in range(len(string)):

            if not string[k:i] in (string, ''):
                print(string[k:i])
                hash_elem = sha256(string[k:i].encode()).hexdigest()
                result.add(hash_elem)
    print(f'{result}')
    print(f'Количество уникальных подстрок в строке "{string}" = {len(result)}\n')


hash_set('papa')
hash_set('utf')
