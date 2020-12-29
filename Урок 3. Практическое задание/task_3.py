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

def string(obj=input("Введите строку: ")):
    set_s = set()
    for i in range(len(obj)):
        set_s.add(sha256(obj[i:].encode('utf-8')).hexdigest())
        set_s.add(sha256(obj[:-i].encode('utf-8')).hexdigest())  
    return len(set_)

print(string())
