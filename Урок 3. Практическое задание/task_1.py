"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import random
import time

list_val = []
dict_val = {}


def timer(func):
    def tmp(*args):
        start_val = time.time()
        res = func(*args)
        print(f'Время выполнения функции: {time.time()-start_val}')
    return tmp


@timer
def rand_list(val):
    print(f'Fil the list.')
    for i in range(val):
        list_val.append(random.randint(0, 100))


@timer
def rand_dict(val):
    print(f'Fil the dict.')
    dict_val.update({a: a for a in range(val)})


@timer
def get_from_dict(val):
    print(f'Read from dict.')
    if val.get('1') is not None:
        print(f'Find')


@timer
def get_from_list(val):
    print(f'Read from list.')
    for z in val:
        if z == '1':
            print('Find')


rand_dict(1000000)
rand_list(1000000)
get_from_dict(dict_val)
get_from_list(list_val)

""" 
Из полученных результатов видно, что не только чтение из словарей быстрее, но и запись, как не странно).
Fil the dict.
Время выполнения функции: 0.19794797897338867
Fil the list.
Время выполнения функции: 1.4266400337219238
Read from dict.
Время выполнения функции: 7.152557373046875e-06
Read from list.
Время выполнения функции: 0.0363161563873291
"""