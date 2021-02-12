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


def time_decorator(func):
    def timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, end - start

    return timer


@time_decorator
def list_func(length):
    result = []
    for i in range(length):
        result.append(i)
    return result


@time_decorator
def dict_func(length):
    result = {}
    for i in range(length):
        result[i] = f'number {i}'
    return result


#new_list_1, list_time_1 = list_func(10)
new_list_1 = list_func(1000)
print (new_list_1)
#new_dict_1, dict_time_1 = dict_func(100000)
#print('LIST 10000: ', list_time_1)
#print('DICT 10000: ', dict_time_1)
