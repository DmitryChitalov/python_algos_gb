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


def time_decorator(func):
    def timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, end - start

    return timer


@time_decorator
def list_func(length):
    result = []
    for i in range(length):
        result.append(i)
    return result


@time_decorator
def dict_func(length):
    result = {}
    for i in range(length):
        result[i] = f'number {i}'
    return result


@time_decorator
def check_dict_key(dict_obj):
    v = dict_obj[3456]
    print(v)


@time_decorator
def check_list_index(list_obj):
    for i in range(len(list_obj)):
        if i == 3456:
            print(list_obj[i])


@time_decorator
def check_dict_value(dict_obj):
    for v in dict_obj.values():
        if v == 'number 3456':
            print(v)


@time_decorator
def check_list_value(list_obj):
    for v in list_obj:
        if v == 3456:
            print(v)


new_list_1, list_time_1 = list_func(10000)
new_dict_1, dict_time_1 = dict_func(10000)
print('LIST 10000: ', list_time_1)
print('DICT 10000: ', dict_time_1)

new_list_2, list_time_2 = list_func(100000)
new_dict_2, dict_time_2 = dict_func(1000000)
print('LIST 100000: ', list_time_2)
print('DICT 100000: ', dict_time_2)

new_list_3, list_time_3 = list_func(1000000)
new_dict_3, dict_time_3 = dict_func(1000000)
print('LIST 1000000: ', list_time_3)
print('DICT 1000000: ', dict_time_3)

print('------------------')

print('Index LIST 10000: ', check_list_index(new_list_1)[1])
print('Keys DICT 10000: ', check_dict_key(new_dict_1)[1])
print('Index LIST 100000: ', check_list_index(new_list_2)[1])
print('Keys DICT 100000: ', check_dict_key(new_dict_2)[1])
print('Index LIST 1000000: ', check_list_index(new_list_3)[1])
print('Keys DICT 1000000: ', check_dict_key(new_dict_3)[1])

print('------------------')

print('Values LIST 10000: ', check_list_value(new_list_1)[1])
print('Values DICT 10000: ', check_dict_value(new_dict_1)[1])
print('Values LIST 100000: ', check_list_value(new_list_2)[1])
print('Values DICT 100000: ', check_dict_value(new_dict_2)[1])
print('Values LIST 1000000: ', check_list_value(new_list_3)[1])
print('Values DICT 1000000: ', check_dict_value(new_dict_3)[1])

