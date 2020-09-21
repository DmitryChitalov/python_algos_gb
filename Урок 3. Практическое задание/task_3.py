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


def count_str():
    my_str = 'papa'
    s_list = []
    s_dict = {}
    for i in range(len(my_str)):
        for j in range(len(my_str) - 1 if i == 0 else len(my_str), i, -1):
            s_list.append(hash(my_str[i:j]))
            s_dict[my_str[i:j]] = hash(my_str[i:j])
    print(s_dict)
    return f' {len(set(s_list))} substrings in string -  {my_str}'


print(count_str())

