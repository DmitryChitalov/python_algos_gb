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

# input_string = "abracadabra"
input_string = "papa"
string_length = len(input_string)
hash_set = set()
for i in range(string_length):
    j = i + 1
    while j <= string_length:
        line_slice = input_string[i:j]
        hash_set.add(hashlib.md5(line_slice.encode()).hexdigest())
        j += 1
hash_set.discard(hashlib.md5(input_string.encode()).hexdigest())  # если из набора подстрок надо удалить полную строку
print(hash_set)
print(f'Строка "{input_string}" содержит {len(hash_set)} уникальных подстрок')
