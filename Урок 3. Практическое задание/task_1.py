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


def function_execution_time(function):
    def time_dec(el):
        start_time = time.time()
        function(el)
        end_val = time.time()
        print(f'Время выполнения функции {function}:  {end_val - start_time}')

    return time_dec


@function_execution_time
def my_list(el):
    my_lst = [i for i in range(el)]
    return my_lst


@function_execution_time
def my_dict(el):
    my_dct = {f'key{i}': i for i in range(el)}
    return my_dct


if __name__ == '__main__':
    dict_1 = my_dict(10000000)
    list_1 = my_list(10000000)

"""

Время выполнения функции <function my_dict at 0x01CF7808>:  6.060662508010864
Время выполнения функции <function my_list at 0x039BD1D8>:  0.6240110397338867
Работа со списками по времения явно быстрей, чем со славарями.
"""
