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

user_string = input("Введите строчку из маленьких латинских букв: ")
end_set = set()
set_length = len(user_string)
for i in range(set_length):
    if i != 0:
        set_length = len(user_string)
    else:
        set_length = len(user_string) - 1
    for j in range(set_length, i, -1):
        print(user_string[i: j])
        end_set.add(hashlib.sha1(user_string[i:j].encode('utf-8')).hexdigest())
print(end_set)
