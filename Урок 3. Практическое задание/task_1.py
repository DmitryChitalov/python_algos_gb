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


def time_count(fn):
    def wrapper(arg):
        start = time.perf_counter()
        fn(arg)
        finish = time.perf_counter() - start
        print(finish)

    return wrapper


@time_count
def fill_list(n):
    list_ = []
    for i in range(10 ** n):
        list_.append(i)


fill_list(6)


@time_count
def fill_dict(n):
    dict_ = {}
    for ind, val in enumerate(range(10 ** n)):
        dict_[str(ind)] = val


fill_dict(6)
