"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        delta_time = end_time - start_time
        print(f'runtime is: {delta_time:.4f} sec')
        return value

    return wrapper_timer


def list_generator(num):
    this_list = list()
    for i in range(num):
        this_list.append(i)
    return this_list


def dict_generator(num):
    this_dict = dict()
    for i in range(num):
        this_dict[i] = i
    return this_dict


@timer
def waste_time_create_list(num_times):
    list_generator(num_times)


@timer
def waste_time_create_dict(num_times):
    dict_generator(num_times)


@timer
def waste_time_on_remove_list(inp_list):
    list_length = len(inp_list)
    for i in range(list_length):
        inp_list.remove(i)


@timer
def waste_time_on_pop_list(inp_list):
    list_length = len(inp_list)
    for _ in range(list_length):
        inp_list.pop()


@timer
def waste_time_on_del_dict(inp_dict):
    dict_length = len(inp_dict)
    for i in range(dict_length):
        del inp_dict[i]


if __name__ == '__main__':
    data_size = 250000
    print('create list,dict:')
    waste_time_create_list(data_size)
    waste_time_create_dict(data_size)
    print('remove list:')
    new_list = list_generator(data_size)
    waste_time_on_remove_list(new_list)
    print('remove pop list:')
    new_list = list_generator(data_size)
    waste_time_on_pop_list(new_list)
    print('remove del dict:')
    new_dict = dict_generator(data_size)
    waste_time_on_del_dict(new_dict)
