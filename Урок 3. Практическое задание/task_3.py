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
initial_date = 'рара'


def sub_string(arg, result_list=[]):
    if len(arg) == 1:
        result_list.append(arg)
        return result_list
    for ind in range(1, len(arg) + 1):
        result_list.append(arg[:ind])
        if ind == len(arg):
            sub_string(arg[1:], result_list=result_list)
    result_list = set(result_list)
    return {str(ind): val for ind, val in enumerate(set(result_list))}


print(sub_string(initial_date))
