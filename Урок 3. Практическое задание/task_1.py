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


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return res

    return wrapper


@benchmark
def init_list():
    lst = []
    for i in range(100000):
        lst.append(i)
    return lst


@benchmark
def init_dict():
    dict = {}
    for i in range(100000):
        dict[i] = i
    return dict


@benchmark
def add_to_list(lst):
    for i in range(100000):
        lst.append(i)


@benchmark
def add_to_dict(dict):
    for i in range(100000, 200000):
        dict[i] = i


@benchmark
def get_from_list(lst):
    return lst[100000]


@benchmark
def get_from_dict(dict):
    return dict.get(100000)


list = init_list()
dict = init_dict()
add_to_list(list)
add_to_dict(dict)
list_el = get_from_list(list)
dict_el = get_from_dict(dict)
