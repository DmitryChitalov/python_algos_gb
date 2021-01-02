"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import time
from random import randint


def stopwatch(func):
    def wrapper(*args, **kwargs):
        t_ns = time.perf_counter_ns()
        t = time.time()
        res = func(*args, **kwargs)
        print(f'{func.__name__} выполнялась {time.time()-t} секунд, {time.perf_counter_ns()-t_ns} наносекунд')
        return res
    return wrapper


@stopwatch
def fill_dict(d, n):
    for i in range(n):
        d[i] = i
    return d


@stopwatch
def fill_list(l, n):
    for i in range(n):
        l.append(i)
    return l


@stopwatch
def dict_get(d, i):
    return d[i]


@stopwatch
def list_get(l, i):
    return l[i]


if __name__ == '__main__':
    my_dict = {}
    my_list = []
    max_items = 10000000
    my_dict = fill_dict(my_dict, max_items)
    my_list = fill_list(my_list, max_items)
    search_n = randint(0, max_items+1)
    print(dict_get(my_dict, search_n))
    print(list_get(my_list, search_n))

# заполнение словаря происходит меделенне, чем списка из-за того, что для добавления элемента в словар необходимо
# рассчитать значение хэша для ключа, добавление в список же не требует каки-либо дополнительных расчетов

