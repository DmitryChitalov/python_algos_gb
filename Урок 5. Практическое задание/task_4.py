"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit


def test(n):
    return {x: x**2 for x in range(n)}


def del_d(param):
    if param is False:
        return d.pop(list(d.keys())[0])
    elif param is True:
        return d.popitem()
    else:
        print(f'Операция остановлена, вы ввели ошибочный параметр!')


def del_od(param):
    if param is False or True:
        return o_d.popitem(last=param)
    else:
        print(f'Операция остановлена, вы ввели ошибочный параметр!')


def sort_d():
    return sorted(d.items(), key=lambda v: v[1])


def sort_od():
    return sorted(o_d.items(), key=lambda v: v[1])


d = test(20000)
o_d = OrderedDict(test(20000))

print(f'-- Delete first item DICT-- \n{timeit("del_d(False)", setup="from __main__ import del_d", number=1000)}')
print(f'-- Delete first item OrderDICT-- \n{timeit("del_od(False)", setup="from __main__ import del_od", number=1000)}\n')

print(f'-- Delete last item DICT-- \n{timeit("del_d(True)", setup="from __main__ import del_d", number=1000)}')
print(f'-- Delete last item OrderDICT-- \n{timeit("del_od(True)", setup="from __main__ import del_od", number=1000)}\n')

print(f'-- Sort DICT-- \n{timeit("sort_d()", setup="from __main__ import sort_d", number=1000)}')
print(f'-- Sort OrderDICT-- \n{timeit("sort_od()", setup="from __main__ import sort_od", number=1000)}\n')


"""
Сомнительная практическая польза от использования OrderedDict, т.к. одна операция только быстрее получается - 
удаление первого элемента из словаря. Я думаю в повседневных задачаз, за глаза хватит встроенного словаря.
"""

