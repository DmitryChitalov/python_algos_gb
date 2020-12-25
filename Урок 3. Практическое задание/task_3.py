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


def substring(string):
    substring_set = set()
    for i in range(len(string) + 1):
        for j in range(len(string) + 1):
            if string[i:j] == string or string[i:j] == '':
                continue
            substring_set.add(hash(string[i:j]))
    return len(substring_set)


st = 'papa'
print(substring(st))

'''
Использовал базовую функцию hash(), так как в рамках одного запуска
a = hash('pa')  # 85432158
b = hash('pa')  # 85432158
print(a == b)  # True
'''
