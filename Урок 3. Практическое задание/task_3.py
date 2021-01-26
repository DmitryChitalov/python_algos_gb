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

test_string = input("Введите строку ")
work_dict = {}
n = len(test_string)
set_0 = set()
for i in range(1, n):
    work_dict[i] = set()
    for j in range(n-i+1):
        work_dict.get(i).add(test_string[j:j+i])
    print(*work_dict[i])

