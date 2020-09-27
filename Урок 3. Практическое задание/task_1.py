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


def time_measure_2(func):
    def g(n):
        time_before = time.time()
        a = func(n)
        time_after = time.time()
        result_time = time_after - time_before
        return result_time
    return g


@time_measure_2
def list_filling(number):
    result_list = []
    for el in range(number):
        result_list.append(random.randint(1, 100000))
    return result_list


@time_measure_2
def dict_filling(number):
    result_dict = {}
    for key in range(number):
        result_dict.setdefault(key, random.randint(1, 100000))
    return result_dict


print(f'Заполнение списка: {list_filling(1000000)}')
print(f'Заполнение словаря: {dict_filling(1000000)}')
