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


def time_counter(func):
    def time_count(*args):
        start_time = time.time()
        result = func(*args)
        finish_time = time.time()
        print(f'Время выполнения функции {func}: {finish_time - start_time} сек')
        return result

    return time_count


@time_counter
def list_fill(el):
    lst = [i for i in range(el)]
    return lst


@time_counter
def dic_fill(el):
    dic = {i: i for i in range(el)}
    return dic


@time_counter
def get_el_list(lst, el):
    return lst[el]


@time_counter
def get_el_dic(dic, el):
    return dic.get(el)


list_1 = list_fill(10000000)
# Время выполнения: 0.8135509490966797 сек

dic_1 = dic_fill(10000000)
# Время выполнения: 1.0064218044281006 сек

get_el_list(list_1, 545643)
# Время выполнения: 0.0 сек

get_el_dic(dic_1, 858434)
# Время выполнения: 0.0 сек

# Таким образом, словарь заполняется дольше, чем список, а операции по
# извлечению элементов из списка и словаря занимают одинаковое количество времени