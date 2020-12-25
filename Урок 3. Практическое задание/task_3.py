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


def substring(string):
    substring_set = set()
    for i in range(len(string)):
        for j in range(len(string)-1 if i == 0 else len(string), i, -1):
            # print(string[i], string[j])
            # print(string[i:j])
            substring_set.add(hashlib.sha256(bytes(string[i:j], 'cp1251')))
    return substring_set


# строка filder
# строка filfil
amount_substing = len(substring(input('Введите строку:\n')))
print(f'Количество различных подстрок в строке: {amount_substing}')


