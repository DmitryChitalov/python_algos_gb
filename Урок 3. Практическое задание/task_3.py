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

s_1 = input('Введите строку: ')

subs_lst = set()

for item in range(len(s_1)):
    for j in range(item, len(s_1)):
        subs_lst.add(hashlib.sha1(s_1[item:j + 1].encode('utf-8')).hexdigest())

print('Количество неповторяющихся подстрок - ', len(list(subs_lst)))
