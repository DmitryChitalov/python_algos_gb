"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import time


def check_time(func):
    def wrapper(n):
        start_time = time.time()
        func(n)
        end_time = time.time()
        print(f'{func.__name__} time is {end_time - start_time}')

    return wrapper


@check_time
def func_list(n):
    a = []
    for i in range(n):
        a.append(i * i)
    return a


@check_time
def func_dict(n):
    a = {}
    for i in range(n):
        a[i] = i * i
    return a


func_list(5)
func_dict(5)
