"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
a
"""

import hashlib

str = input("Введите строку из маленьких латинских букв: ")

result_set = set()
for v_s in range(len(str)):
    last_str = str[v_s:]
    for length in range(1, len(last_str) + 1):
        sub_str = str[v_s:v_s + length]
        if str != sub_str:
            hash_sub_str = hash(sub_str)
            result_set.add(hash_sub_str)

print(len(result_set))

print(f"Количество различных подстрок в строке {str} : {len(result_set)}")
