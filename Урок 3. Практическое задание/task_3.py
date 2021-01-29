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


def substrings(s):
    res_hash = set()
    res = set()

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            print(s[i:j])
            res_hash.add(hash_the_object(s[i:j]).decode())
            res.add(s[i:j])

    res_hash.remove(hash_the_object(s).decode())
    res.remove(s)
    return res_hash, res

