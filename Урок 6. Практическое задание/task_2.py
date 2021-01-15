"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, библиотеки) для оптимизации памяти и
доказать! (наглядно, кодом) их эффективность (на примере профилировщика)
"""
from collections import namedtuple
from memory_profiler import profile
from random import randint
from sys import getsizeof


# Можно  предположить что если кортежи  у нас используют меньше памяти  то и namedtuple будут  использовать меньше.
# В ряде задач их можно использовать вместо словарей

# @profile()
def use_dict(*args):
    test_dict = {}
    for arg in args:
        test_dict.update([(arg, randint(0, 500))])
    return test_dict


# @profile()
def use_n_tuple(*args):
    Tuple_obj = namedtuple('new_name', f'{",".join([i for i in args])}')
    test_tuple = Tuple_obj(*(randint(0, 500) for k in args))
    return test_tuple


def get_one(test_obj, el_name):
    if type(test_obj) == dict:
        return test_obj.get(el_name)
    else:
        return getattr(test_obj, el_name)


# просто проверить что можно элемент по ключу вернуть. можно


if __name__ == '__main__':
    a = use_n_tuple('x', 'y', 'z')
    print(a)
    print(getsizeof(a))

    b = use_dict('x', 'y', 'z')
    print(b)
    print(getsizeof(b))

    print(get_one(a, 'x'))
    print(get_one(b, 'x'))

    """
    профайлер на таком датасете ничего внятного не показал, но итоговый обьект по размеру отличается почти в 4 раза, 
    и  namedtuple хоть с ним и сложней работать, более компактный, при этом можно использовать его вместо словаря,
    если нужно только чтение
    
    Win10x64, Python 3.9.0
    """
