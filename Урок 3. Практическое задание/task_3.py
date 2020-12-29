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
from hashlib import sha1


string = input('Введите строку из строчных букв:  ')
set_substr = set()

for i in range(0, len(string)):
    for j in range(len(string), i, -1):
        set_substr.add(sha1(string[i:j].encode()).hexdigest())
set_substr.remove(sha1(string.encode()).hexdigest())
print(f'Количество различных подстрок - {len(set_substr)}')