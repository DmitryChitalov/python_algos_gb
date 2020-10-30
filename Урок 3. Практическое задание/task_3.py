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

string = 'papa'
hash_string = hashlib.sha256(bytes(string, 'utf-8')).hexdigest()

list_ = set()
for i in range(len(string)):
    for ii in range(len(string) + 1):
        temp_str = hashlib.sha256(bytes(string[i:ii], 'utf-8')).hexdigest()
        if temp_str != hash_string and string[i:ii] != '':
            list_.add(string[i:ii])
print(len(list_))

