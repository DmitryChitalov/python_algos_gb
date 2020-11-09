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

input_string = input('Введите строку: ')
substring_hash_list = []


def rec_substring(c=0, h=1):
    if c < len(input_string):
        for i in range((len(input_string))):
            if len(input_string[i:h + i]) == c + 1:
                substring_hash_list.append(sha256(input_string[i:h + i].encode("utf-8")).hexdigest())
        return rec_substring(c + 1, h + 1)
    else:
        return


rec_substring()
print(f'Количество уникальных подстрок в строке: {len(set(substring_hash_list))} варианта(ов).')
