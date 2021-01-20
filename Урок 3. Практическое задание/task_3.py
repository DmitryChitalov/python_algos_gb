"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

раnama:




"""

from hashlib import sha256

test_string = 'panama'
subs = set()


def test(my_string, start=0, stop=1):
    while start < len(my_string):
        if stop < len(my_string):
            subs.add(sha256(my_string[start:stop].encode('utf-8')).hexdigest())
            stop += 1
        else:
            start += 1
            subs.add(sha256(my_string[start:stop].encode('utf-8')).hexdigest())
            stop = start + 1


test(test_string)
print(subs)

