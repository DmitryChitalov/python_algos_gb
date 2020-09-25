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


def func_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f'Время выполнения {end}')
        return result
    
    return wrapper


@func_timer
def append_list(elem):
    list_el = []
    for i in range(elem):
        list_el.append(i)
    print(list_el)
    return list_el


@func_timer
def append_dict(elem):
    dict_el = {}
    for i in range(elem):
        dict_el[i] = i
    print(dict_el)
    return dict_el


@func_timer
def remove_list(list_el):
    list_el.remove(100)
    return list_el


@func_timer
def remove_dict(dict_el):
    dict_el.pop(100)
    return dict_el


list = append_list(1000)
dict = append_dict(1000)

remove_dict(dict)
remove_list(list)

# Время заполнения списка быстрее нежели чем у словаря, а время удаления элементана оборот быстрее у словаря, нежели чем у списка