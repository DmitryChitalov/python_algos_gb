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


def count_number_distinct(val):
    _list = []
    for i in range(0, len(val)):
        for j in range(i, len(val)):
            _list.append(sha256(val[i:j].encode('utf-8')).hexdigest())
    return len(set(_list))


# user_input = input('Введите строку: ')
user_input = 'papa'
print(f'Количество различных подстрок в строке "{user_input}" = {count_number_distinct(user_input)}')
