"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit


def test_dict():
    my_dict = {}
    for i in range(1000):
        my_dict[i] = i*i
    # print(my_dict)
    for i in range(1000):
        my_dict.pop(i)
    return True


def test_order():
    my_dict = OrderedDict()
    for i in range(1000):
        my_dict[i] = i*i
    # print(my_dict)
    for i in range(1000):
        my_dict.popitem()
    return True


print(
    timeit(
        "test_dict()",
        setup='from __main__ import test_dict',
        number=10000))  # 2.761655318

print(
    timeit(
        "test_order()",
        setup='from __main__ import test_order',
        number=10000)) # 3.791548501
'''Прочитав методичку и дополнительную информацию в интернете, главная фишка OrderedDict
уже не так актуальна, а из полезных функций стоит отметить move_to_end(key, last=True). Так что не особо
вижу применение этой коллекции в работе.'''
test_order()
test_dict()