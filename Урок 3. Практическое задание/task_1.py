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
import random


def f_time(func):
    def g(n):
        time_before = time.time()
        a = func(n)
        time_after = time.time()
        result_time = time_after - time_before
        return result_time
    return g


@f_time
def list_filling(number):
    result_list = []
    for el in range(number):
        result_list.append(random.randint(1, 100000))
    return result_list


@f_time
def dict_filling(number):
    result_dict = {}
    for key in range(number):
        result_dict.setdefault(key, random.randint(1, 100000))
    return result_dict


print(f'List: {list_filling(1000000)}')
print(f'Dict: {dict_filling(1000000)}')