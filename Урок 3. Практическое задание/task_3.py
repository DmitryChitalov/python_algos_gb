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


def hashes(str, interval):  # ширина среза 1
    hash_dict = {}
    while interval < len(str):  # логично, что можно заменить на рекурсию)
        for i in range(len(str) - interval + 1):
            a = str[i:i + interval]  # срезаю и двигаюсь на 1 вправо
            if hash(a) not in hash_dict.keys():
                hash_dict[hash(a)] = f'{a}'  # потому что просили решить используя хэш сравнения
        interval += 1  # увеличиваю ширину среза
    # print(v for v in hash_dict.values()) <-- не работает :(
    for v in hash_dict.values():
        print(v)


string = input('Write any string containing latin letters only: ')

hashes(string, 1)

'''Работает для любых знаков'''
