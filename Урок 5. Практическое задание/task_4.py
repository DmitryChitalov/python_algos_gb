"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from random import randint
import collections
from timeit import timeit


def fill_dict(n):
    nums_dic = {i: i for i in range(n)}
    return nums_dic


def fill_order_dict(n):
    nums_dic = collections.OrderedDict({i: i for i in range(n)})
    return nums_dic


print('создание словаря')
print(timeit("fill_dict(10)", globals=globals(), number=10000))
print(timeit("fill_order_dict(10)", globals=globals(), number=10000))
'''
По замерам создание словаря быстрее чем создание OrderedDict
'''

my_dic = fill_dict(100000)
my_ord_dic = fill_order_dict(100000)

def popitem_dict(dic):
    return dic.popitem()

def popitem_orderdict(dic):
    return dic.popitem(last=True)


print('извлечение последнего элемента')
print(timeit("popitem_dict(my_dic)", globals=globals(), number=10000))
print(timeit("popitem_orderdict(my_ord_dic)", globals=globals(), number=10000))

'''
При обычсном словаре метод popitem работает быстрее
'''
print('извлечение первого элемента')
def pop_first_dict(dic):
    list(dic.keys())
    return (list(dic.keys())[0], dic.pop(list(dic.keys())[0]))

def pop_first_orderdict(dic):
    return dic.popitem(last=False)

# print(pop_first_dict(my_dic))
# print(pop_first_orderdict(my_ord_dic))
print(timeit("pop_first_dict(my_dic)", globals=globals(), number=10000))
print(timeit("pop_first_orderdict(my_ord_dic)", globals=globals(), number=10000))
'''
Специальный метод можно получать первый элемент, просто заменой last=False а для обычного словаря такого метода нет
нужно переберать через цикл и возвращать первые елементы. Поэтому этот метод работает в разы быстрее в ordereddict
'''