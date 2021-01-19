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

def timeit(func):
    def wrap(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f'Время выполнения {func.__name__}: {end - start}')
        return result
    return wrap

@timeit
def create_list(n):
    lst = [random.randrange(0, 1000) for _ in range(n)]
    return lst

@timeit
def create_dict(n):
     dc = {i: random.randrange(0, 1000) for i in range(n)}
     return dc

@timeit
def get_odd_el_list(lst):
    """ Выборка четных чисел списка"""
    odd_lst = []
    for el in lst:
        if el % 2:
            odd_lst.append(el)
    return odd_lst
@timeit
def get_odd_el_dict(dc):
    """ Выборка четных чисел словаре"""
    odd_lst = []
    for el in dc.values():
        if el % 2:
            odd_lst.append(el)
    return odd_lst

my_dict = create_dict(100000) # 0.1029367446899414
my_list = create_list(100000) # 0.09194207191467285

get_odd_el_dict(my_dict) # 0.006997823715209961
get_odd_el_list(my_list) # 0.005992412567138672

""" Создание словаря происходит медленнее, 
так как помимо значения в него вкладывается ключ, 
при каждом вложении которого вычисляется хеш и проверяется его уникальность.

Функция, отбирающая все четные значения, 
тоже отработала чуть медленнее в словаре, чем в списке. 

"""
