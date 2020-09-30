"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: если вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import time


def measure_time(func):
    def time_stamp(*args):
        start_time = time.time()
        func(args[0])
        print(f'Затраты времени = {time.time() - start_time}')

    return time_stamp


@measure_time
def measure_list(value):
    list_obj = []
    for i in range(value):
        list_obj.append(i)
        list_obj.index(i)
    return list_obj


@measure_time
def measure_dict(value):
    dict_obj = dict()
    for i in range(value):
        dict_obj[i] = i
        dict_obj.get(i)
    return dict_obj


measure_list(25000)
measure_dict(25000)
