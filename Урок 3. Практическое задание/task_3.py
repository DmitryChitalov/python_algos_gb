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


string = input('Введите строку:  ')
result = set()
length = len(string)
for i in range(length):
    if i == 0:
        length = len(string) - 1
    else:
        length = len(string)
    for j in range(length, i, -1):
        print(string[i:j])
        result.add(hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())
print(f'Количество уникальных подстрок {len(result)}')

