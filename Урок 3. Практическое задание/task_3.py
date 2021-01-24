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


def count_substr(string):
    lenght = len(string)
    my_set = set()
    for i in range(lenght):
        if i == 0:
            lenght = len(string) - 1
        else:
            lenght = len(string)
        for j in range(lenght, i,  -1):
            my_set.add(hash(string[i:j]))
    return print(f'Количество различных подстрок: {len(my_set)}')


my_string = input('enter: ')
count_substr(my_string)
