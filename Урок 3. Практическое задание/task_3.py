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

my_string = input('Введите строку: ')
result = set()

elem_string = len(my_string)
for i in range(elem_string):
    if i == 0:
        elem_string = len(my_string) - 1
    else:
        elem_string = len(my_string)
    for j in range(elem_string, i, -1):
        # print(my_string[i:j])
        result.add(hashlib.sha1(my_string[i:j].encode('utf-8')).hexdigest())
# print(result)

print(f'Количество уникальных вхождений в строке \"{my_string}\" равно {len(result)}')
