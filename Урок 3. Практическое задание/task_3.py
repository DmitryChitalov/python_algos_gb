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

def count_substrings(s, storage_set=set()):
    if len(s) == 0:
        return len(storage_set) - 1
    else:
        for i in range(len(s)):
            storage_set.add(hash(s[i:]))
        return count_substrings(s[:-1], storage_set)

string = input('Введите строку для подсчета подстрок: ')
print(f'Количество подстрок составляет: {count_substrings(string)}')