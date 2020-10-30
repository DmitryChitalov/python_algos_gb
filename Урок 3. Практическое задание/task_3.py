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

substring_set = set()
string = input('Введите строку из строчных латинских букв: ')
str_len = len(string)
for i in range(str_len):
    for j in range(str_len):
        if j >= i:
            substr = string[i:j + 1]
            if substr != string:
                hash_substr = hashlib.md5(substr.encode('utf-8')).hexdigest()
                if hash_substr not in substring_set:
                    print(substr)
                substring_set.add(hash_substr)

print(f'\nКоличество подстрок - {len(substring_set)}')
