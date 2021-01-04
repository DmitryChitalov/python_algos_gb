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


def time_dif(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(args[0])
        print(time.time() - start_time)
    return wrapper


@time_dif
def list_gen(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list


@time_dif
def list_read(my_list=[]):
    for i in range(len(my_list) - 1):
        my_list.index(i)


@time_dif
def dict_gen(n):
    my_dict = {}
    for i in range(n):
        my_dict[i] = i


@time_dif
def dict_read(my_dict={}):
    for el in my_dict.keys():
        my_dict.get(el)


test_list = list(i for i in range(10000))
test_dict = dict()
for i in range(10000):
    test_dict[i] = i

print(f'Время создания списка:')
list_gen(10000)  # 0.0009846687316894531
print(f'Время чтения списка:')
list_read(test_list)  # 0.5345711708068848
print(f'Время создания словаря:')
list_gen(10000)  # 0.0019948482513427734 - время сокращается при повторном запуске с одинаковым числом, но, в среднем, словарь генерируется дольше
print(f'Время чтения словаря:')
list_read(test_list)  # 0.5335988998413086

