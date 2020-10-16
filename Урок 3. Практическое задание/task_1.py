"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: если вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
from time import time


def time_func(f):
    def wrapper(*args, **kwargs):
        st = time()
        res = f(*args, **kwargs)
        print(time() - st)
        return res
    return wrapper


@time_func
def create_list(n):
    lst = []
    for i in range(n):
        lst.append(i)
    return lst


@time_func
def create_dict(n):
    dct = dict()
    for i in range(n):
        dct[i] = i
    return dct


@time_func
def read_list(lst, n):
    for i in range(n):
        lst.index(i)


@time_func
def read_dict(dct, n):
    for i in range(n):
        dct.get(i)


el_cnt = 10000

print('Создание списка:')
Lst = create_list(el_cnt)
print('Создание словаря:')
Dct = create_dict(el_cnt)

print('Чтение списка:')
read_list(Lst, el_cnt)
print('Чтение словаря:')
read_dict(Dct, el_cnt)
