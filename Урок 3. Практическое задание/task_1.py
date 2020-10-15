"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: если вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import time


def print_lead_time(decorated_function):
    def my_function(x, y=None):
        start_time = time.time()
        decorated_function(x, y)
        finish_time = time.time()
        print(f'{(finish_time - start_time)}')

    return my_function


@print_lead_time
def put_in_list(input_list, input_data):
    print('Заполнение списка выполнено за ', end='')
    for el in input_data:
        input_list.append(el)
    return input_list


@print_lead_time
def get_from_list(input_list, input_data=None):
    print('Получение элементов списка выполнено за ', end='')
    for el in input_list:
        input_list.index(el)
    return input_list


@print_lead_time
def put_in_dict(input_dict, input_data):
    print('Заполнение словаря выполнено за ', end='')
    for el in input_data:
        input_dict[el] = el


@print_lead_time
def get_from_dict(input_dict, input_data=None):
    print('Плучение элементов словаря выполнено за ', end='')
    for el in input_dict:
        input_dict.get(el)


test_str = b = [i for i in range(30000)]

test_list = []
put_in_list(test_list, test_str)
get_from_list(test_list)

test_dict = {}
put_in_dict(test_dict, test_str)
get_from_dict(test_dict)


'''Вывод: Получение элементов слоаваря выполняется значительно бычтрее, чем получение элементов списка. 
Однако при больших объемах вычислений становиться заметно, что заполнение словаря происходит медленне,
чем заполнение списка. Т.о. для операций с частым поиском/чтением словари являются более быстродейственным решением.'''
