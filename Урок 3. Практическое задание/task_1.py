"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

from time import time


def stopwatch(data):
    def tmp(*args, **kwargs):
        t = time()
        res = data(*args, **kwargs)
        print(f"Time to complete: {round(time() - t, 6)}")
        return res

    return tmp


@stopwatch
def list_stopwatch(num):
    my_list = [i for i in range(num)]
    print(len(my_list), type(my_list))


@stopwatch
def dict_stopwatch(num):
    n = range(num)
    my_dict = {i: x for i, x in zip(n, n)}
    print(len(my_dict), type(my_dict))


list_stopwatch(1000000)
dict_stopwatch(1000000)
