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

test_dict = {}
test_list = []


def timer(func):
    def wrapper(*args):
        start_time = time()
        func(*args)
        end_time = time()
        print(f'Время выполнения функции {str(func)} :  {end_time-start_time}')
    return wrapper

@timer
def fill_list(list, size):
    for i in range(size):
        list.append(i)
    return test_list

@timer
def fill_dict(dic,size):
    for i in range(size):
        dic[i] = i
    return dic



@timer
def get_item_list(list_1):
    for i in range(len(list_1)):
        el = list_1.index(i)


@timer
def get_item_dict(dic):
    for i in range(len(dic)):
        el = dic.get(i)



m = 10**4

fill_list(test_list,m)
fill_dict(test_dict,m)

get_item_list(test_list)
get_item_dict(test_dict)

"""Выводы:
Словарь и список заполняются почти одинаково быстро(словарь немного дольше)
Доступ к элементам в словаре быстрее

"""