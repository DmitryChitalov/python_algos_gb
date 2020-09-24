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
        print(f'Время выполнения {func}: {end}')
        return result

    return wrapper


@func_timer
def create_list():
    result = [el for el in range(1, 10000000)]
    return result


@func_timer
def create_dict():
    result = {el: el for el in range(1, 10000000)}
    return result


@func_timer
def remove_list(_list):
    _list.remove(10000)
    return _list


@func_timer
def remove_dict(_dict):
    _dict.pop(10000)
    return _dict


@func_timer
def append_list(_list):
    _list.append(1000)
    return _list


@func_timer
def update_dict(_dict):
    _dict.update({'10000001': '10000001'})
    return _dict


my_list = create_list()
my_dict = create_dict()

remove_list(my_list)
remove_dict(my_dict)
append_list(my_list)
update_dict(my_dict)


"""
Результат: создавать список значительно быстрее, чем словарь. Поиск и удаление элемента же, напротив, значительно
быстрее происходит у словаря. 
"""
