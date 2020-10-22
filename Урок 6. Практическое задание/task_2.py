"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
from itertools import islice
from memory_profiler import profile
'''
Кроме перечисленных на занятии методов оптимизации, также можно использовать:

Модуль itertools и islice - объект-итератор, 
с помощью которого можно в том числе перебирать срез генератора.
'''

# Пример


def gen():
    n = 0
    while n < 100000:
        n += 1
        yield n


'''
Если попытаться итерировать срез генератора, то возникнет ошибка

nums = [i for i in gen()[:3]]

Используя islice мы избегаем этой ошибки
'''


@profile
def ex_1():
    nums = [i for i in gen()]
    return nums


@profile
def ex_2():
    nums = [i for i in islice(gen(), 5000, 10000)]
    return nums


ex_1()
ex_2()

'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    41     15.5 MiB     15.5 MiB           1   @profile
    42                                         def ex_1():
    43     18.1 MiB      2.6 MiB      100003       nums = [i for i in gen()]
    44     18.1 MiB      0.0 MiB           1       return nums


Filename: D:/Lessons/python_projects/algos/#6/#6_task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    47     15.7 MiB     15.7 MiB           1   @profile
    48                                         def ex_2():
    49     15.8 MiB      0.0 MiB        5003       nums = [i for i in islice(gen(), 5000, 10000)]
    50     15.8 MiB      0.0 MiB           1       return nums
'''