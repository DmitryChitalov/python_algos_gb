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

def substring_calc(string):
    list_of_hashes = []
    for i in range(len(string)+1):
        for j in range(len(string)+1):
            element = string[i:j]
            if element == '' or element == string:
                continue
            else:
                list_of_hashes.append(element)
    return set(list_of_hashes)
print(substring_calc('раращо'))
