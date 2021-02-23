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


def dec_time(f):
    def wrapper(*args, **kwargs):
        t1 = time()
        res = f(*args, **kwargs)
        t2 = time()
        return res, (t2 - t1)

    return wrapper


@dec_time
def list_create(n):
    res = []
    for i in range(n):
        res.append(i)
    return res


@dec_time
def dict_create(n):
    res = {}
    for i in range(n):
        res[i] = i
    return res


@dec_time
def get_by_index_dict(v, obj):
    return obj[v]


@dec_time
def get_by_index_list(v, obj):
    for i in range(len(obj)):
        if i == v:
            return (obj[i])

@dec_time
def get_by_value_dict(v,obj):
    for i in obj.values():
        if i == v:
            return v

@dec_time
def get_by_value_list(v, obj):
    for i in obj:
        if i == v:
            return i



l = [10000, 40000, 100000]

for k in l:
    first_list, first_list_time = list_create(k)
    first_dict, first_dict_time = dict_create(k)

    print('if {} in list'.format(k), first_list_time)
    print('if {} in dict'.format(k), first_dict_time)
    print('Get by index list', get_by_index_list(k - 1, first_list))
    print('Get by index dict', get_by_index_dict(k - 1, first_dict))
    print('Get by value list', get_by_value_list(k-1, first_list))
    print('Get by value dict', get_by_value_dict(k-1, first_dict))
    print()

    #Заполнение листа происходит быстрее т.к. он не хэширует,
    # но вот работа с данными уже происходит быстрее уже в словаре т.к. перебор и обращение к данным словаря быстрее