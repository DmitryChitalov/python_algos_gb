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
import hashlib as h
s = 'рара'
my_set = set()

def my_hash(s):
    return h.sha1(s.encode('utf-8')).hexdigest()

def check_str(string):
    for i in range(1, len(string)):
        for j in range(len(string)):
            if my_hash(string[j:i+j]) in my_set:
                continue
            else:
                my_set.add(my_hash(string[j:i+j]))
                print(string[j:i+j])
    return

check_str(s)