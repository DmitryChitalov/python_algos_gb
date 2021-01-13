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

user_str = 'papa'
my_set = set()

try:
    for x in range(len(user_str)):
        word = ''
        for i in user_str[x:]:
            word += i
            if word == user_str:
                continue
            hash_obj = hashlib.sha256(word.encode('utf-8'))
            res = hash_obj.hexdigest()
            my_set.add((res, word))
except IndexError:
    my_set.add(user_str[-1])

for i in my_set:
    print(i)
