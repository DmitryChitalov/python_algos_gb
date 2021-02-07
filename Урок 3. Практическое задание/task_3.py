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


def my_string(string, list_hash=set()):
    if len(string) == 0:
        return list_hash
    else:
        n = len(string)
        while n != 0:
            b = string[:n]
            n -= 1
            res = hash(b)
            list_hash.add(res)
        return my_string(string[1:], list_hash)


print(my_string(input("Введите строку состоящую только из строчных латинских букв: ")))
