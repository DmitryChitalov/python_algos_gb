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


def time_dec(func):
    def g(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        stop = time()
        print(f"Время выполнения - {stop - start}")

        return result

    return g


@time_dec
def fill_list(num_elems):
    return list(i for i in range(num_elems))


@time_dec
def fill_dict(num_elems):
    return {i: i for i in range(num_elems)}


"""
Время заполнения словаря больше, чем списка, т.к. при создании ключа в словаре генерируется его хеш
и добавляется в хеш-таблицу
"""
fill_list = fill_list(100)
fill_dict = fill_dict(100)


@time_dec
def from_dict(dict: dict, key):
    return dict[key]


@time_dec
def from_list(list: list, key):
    return list[key]


@time_dec
def getall_from_dict(dict: dict):
    for key, value in dict.items():
        print(f"{key}:{value}")


@time_dec
def getall_from_list(list: list):
    for i in list:
        print(i)


print(from_dict(fill_dict, 1))
print(from_list(fill_list, 2))
print(getall_from_dict(fill_dict))
print(getall_from_list(fill_list))

"""
По результатам получение данных из словарей быстрее, чем из списков, т.к. в словарях используется хещ-дерево
"""
