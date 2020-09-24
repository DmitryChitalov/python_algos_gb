"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

from timeit import timeit


array = [1, 3, 1, 3, 4, 5, 1]


"""Самый эффективный т.к. не содержит лишних действий"""


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


"""Быстрее не получилось((("""


def my_func():
    indexes = [(array.count(x), x) for x in set(array)]
    elem = sorted(indexes)[-1][1]
    return f'func_3 - Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'


print(func_1())
print(func_2())
print(my_func())
print(timeit('func_1()', 'from __main__ import func_1', number=10000))
print(timeit('func_2()', 'from __main__ import func_2', number=10000))
print(timeit('my_func()', 'from __main__ import my_func', number=10000))
