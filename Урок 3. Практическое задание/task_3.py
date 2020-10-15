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


def str_func(inp_str, substring_set=None):
    if substring_set is None:
        substring_set = set()
    for i in range(len(inp_str)):
        for j in range(len(inp_str) - 1 if i == 0 else len(inp_str), i, -1):
            sub_str = inp_str[i:j]
            sub_str_hash = sha256(sub_str.encode()).hexdigest()
            substring_set.add(sub_str_hash)
            print(f'Строка - "{sub_str}", '
                  f'хеш - "{sub_str_hash}"')
    return len(substring_set)


print(f'Количество подстрок в строке: {str_func(inp_str=input("Введите строку: "))}')
