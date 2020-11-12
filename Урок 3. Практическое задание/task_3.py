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

def count_str (arg):
    sp = []
    for k in range(0,len(arg)):
        for i in range(k+1,len(arg)+1):
            sp.append(hashlib.sha256(arg[k:i].encode()).hexdigest())
    print(sp)
    sp = set(sp)
    print(sp)
    print(f'Количество подстрок  {len(sp)-1}')  #-1 берется для поправки на исключение исходного слова из подстрок

count_str('')