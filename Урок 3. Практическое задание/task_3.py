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

some_set = set()
some_str = 'papa'
for i in range(len(some_str)):
    for j in range(i + 1, len(some_str)+1):
        if some_str[i:j] != some_str:
            some_set.add(hashlib.sha256(some_str[i:j].encode()).hexdigest())
            print(some_str[i:j], end=' ')
print(f'\n{some_set}')
print(f'Количество элементов в множестве: {len(some_set)}')
