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

string = input('Введите строку:')
sub_str = set()
first_iter = 1
for i in range(len(string)):
    for j in range(i + 1, len(string) + 1 - first_iter):
        sub_str.add(hashlib.sha256(string[i:j].encode()).hexdigest())
    first_iter = 0
print(f'Количество уникальных подстрок = {len(sub_str)}')

