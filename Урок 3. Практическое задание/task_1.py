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


def test_time(our_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        our_func(args[0])
        print(time.time() - start)
    return wrapper


@test_time
def test_list(n):
    our_list = []
    for i in range(n):
        our_list.append(i)
    return our_list


@test_time
def test_dict(n):
    our_dict = dict()
    for i in range(n):
        our_dict[i] = i
    return our_dict


test_list(500000)
test_dict(500000)
