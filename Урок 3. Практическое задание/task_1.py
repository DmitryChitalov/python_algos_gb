"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

from timeit import default_timer
from random import randrange


def time_ctr(func):
    def inner(*args, **kwargs):
        begin = default_timer()
        res = func(*args, **kwargs)
        end = default_timer()

        print(f'Time {(end - begin)}')
        return res

    return inner


@time_ctr
def new_list(val_num):
    res = []
    for i in range(val_num):
        res.append(randrange(i, val_num))

    return res


@time_ctr
def new_dict(val_num):
    res = {}
    for i in range(val_num):
        res[randrange(i, val_num)] = i

    return res


@time_ctr
def search_list_item(lst):
    for i in range(len(lst) - 1):
        r = i in lst


@time_ctr
def search_dict_item(d):
    for i in range(len(d) - 1):
        r = d.get(i)


if __name__ == '__main__':
    val_num = 100000

    # --------------Словарь---------------------------
    # 1000 - Time 0.002132800000000004
    # 10000 - Time 0.0252579
    # 100000 - Time 0.2743738
    dct = new_dict(val_num)

    # 1000 - Time 0.00011139999999999761
    # 10000 - Time 0.0011748000000000036
    # 100000 - Time 0.013481899999999991
    search_dict_item(dct)

    # --------------Список----------------------------
    # 1000 - Time 0.003819900000000001
    # 10000 - Time 0.022004499999999996
    # 100000 - Time 0.27407780000000004
    ls = new_list(val_num)

    # 1000 - Time 0.02463470000000001
    # 10000 - Time 2.2486102
    # 100000 - Time 271.5878309
    search_list_item(ls)

# Вывод: добавление элемента в список и словарь происходит за константтое время, поиск по ключу
# словаре за константное время, значения в списке O(n)
