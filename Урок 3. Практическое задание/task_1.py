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

# реализация без декоратора


def filling_in_the_list(num_elems):
    completed_list = []
    start = time.time()
    for i in range(num_elems):
        completed_list.append(i)
    end = time.time()
    delta_time = end - start
    return completed_list, delta_time


def filling_in_the_dict(num_elems):
    completed_dict = {}
    start = time.time()
    for i in range(num_elems):
        completed_dict[i] = i
    end = time.time()
    delta_time = end - start
    return completed_dict, delta_time


def get_value_from_list(list_obj):
    start = time.time()
    for num_elem in range(len(list_obj) - 1):
        list_obj.index(num_elem)
    end = time.time()
    return end - start


def get_value_from_dict(dict_obj):
    start = time.time()
    keys = list(dict_obj.keys())
    for num_item in range(len(keys) - 1):
        dict_obj.get(num_item)
    end = time.time()
    return end - start


# реализация с декоратором
def time_speed(func_obj):
    def wrapper(*args, **kwargs):
        start = time.time()
        func_obj(args[0])
        end = time.time()
        print(f'Время работы функции: {end - start}')
    return wrapper


@time_speed
def filling_in_the_list_2(num_elems):
    completed_list = []
    for i in range(num_elems):
        completed_list.append(i)
    return completed_list


@time_speed
def filling_in_the_dict_2(num_elems):
    completed_dict = {}
    for i in range(num_elems):
        completed_dict[i] = i
    return completed_dict


@time_speed
def get_value_from_list_2(list_obj):
    for num_elem in range(len(list_obj) - 1):
        list_obj.index(num_elem)


@time_speed
def get_value_from_dict_2(dict_obj):
    keys = list(dict_obj.keys())
    for num_item in range(len(keys) - 1):
        dict_obj.get(num_item)


if __name__ == '__main__':
    num_elements = 10000
    res_list, time_filling_list = filling_in_the_list(num_elements)
    print(f'Время заполнения списка: {time_filling_list}')
    res_dict, time_filling_dict = filling_in_the_dict(num_elements)
    print(f'Время заполнения словаря: {time_filling_dict}')

    print(f'Время обработки списка: {get_value_from_list(res_list)}')
    print(f'Время обработки словаря: {get_value_from_dict(res_dict)}')
    filling_in_the_list_2(num_elements)
    filling_in_the_dict_2(num_elements)
    get_value_from_list_2(res_list)
    get_value_from_dict_2(res_dict)

"""
Выводы: Заполнение списка и словаря происходят примерно с одинаковыми временными затратами,
а получение значений из словаря, гораздо быстрее, чем из списка.
Декоратор очень сильно экономит код и облегчает анализ временного анализа работы функций.
"""