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


def substrings(user_d):
    set_substrings = set()
    count = len(user_d)
    for el in range(len(user_d)):
        for i in range(len(user_d)):
            if user_d not in user_d[i:i+count]:
                set_substrings.add(hashlib.sha256(user_d[i:i+count].encode('utf-8')).hexdigest())
        count -= 1
    return set_substrings


user_data = input("Введите строку состоящую только из строчных латинских букв: ")
print(f"Количество подстрок: {len(substrings(user_data))}")

