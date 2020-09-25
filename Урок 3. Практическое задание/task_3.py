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

some_dict = set()

string_txt = "papa"
for x in range(len(string_txt)):
    for y in range(x, len(string_txt)):
        string_to_hash = hashlib.sha256(string_txt[x:y+1].encode())
        some_dict.add(string_to_hash.hexdigest())
print(f'Result: string {string_txt} get {len(some_dict)} the same substrings'