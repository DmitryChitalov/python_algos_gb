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


def compare(first, second):
    return first.hash() == second.hash()


s = input('Введите строку: ')
substrings = (s[i:j+1] for i in range(len(s)) for j in range(len(s)))
unique_substrings = set()
for ss in substrings:
    # смысла в этой проверке нет, если просто добавлять в множество, то на выходе будут только уникальные
    already_exists = False
    for us in unique_substrings:
        if hash(us) == hash(ss):
            already_exists = True
    if not already_exists:
        unique_substrings.add(ss)

print(unique_substrings)
