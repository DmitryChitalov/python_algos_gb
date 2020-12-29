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


def timer_dec(fn):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        res = fn(*args, **kwargs)
        print(time.time() - time_start)
        return res
    return wrapper


@timer_dec
def fill_dict_comp(num):
    return {el: el for el in range(num)}


@timer_dec
def fill_dict(num):
    new_dict = {}
    for i in range(num):
        new_dict.update({i: i})
    return new_dict


@timer_dec
def fill_list_comp(num):
    return [el for el in range(num)]


@timer_dec
def fill_list(num):
    new_lst = []
    for i in range(num):
        new_lst.append(i)
    return new_lst


print('Словари:')
my_dict1 = fill_dict(10000)         # 0.0038297176361083984
my_dict2 = fill_dict_comp(10000)    # 0.0017733573913574219

print('Списки:')
my_lst1 = fill_list(10000)          # 0.0013060569763183594
my_lst2 = fill_list_comp(10000)     # 0.0007607936859130859

# Вывод: словари формируются дольше, чем списки

