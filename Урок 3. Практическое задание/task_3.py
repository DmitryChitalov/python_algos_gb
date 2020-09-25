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

new_list = input('Введите слово')
lists = []
for i in range(0, len(new_list) + 1):
    for i_2 in range(i + 1, len(new_list) + 1):
        lists.append(hashlib.sha1(new_list[i:i_2].encode('utf-8')).hexdigest())

lists.remove(hashlib.sha1(new_list.encode('utf-8')).hexdigest())

print(f'Колличество различных подстрок в строке {new_list} равно {len(set(lists))}')