"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

from timeit import timeit
from numpy import argmax, bincount

array = [1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5]


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


def func_3():
    m = 0
    num = 0
    for i in set(array):
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_4():
    m = bincount(array)
    num = argmax(m)
    return f'Чаще всего встречается число {num},' \
           f'оно появилось в массиве {max(m)} раз(а)'


print('func_1')
print(func_1())
print(timeit("func_1()", setup="from __main__ import func_1", number=100000))

print('func_2')
print(func_2())
print(timeit("func_2()", setup="from __main__ import func_2", number=100000))

print('func_3')
print(func_3())
print(timeit("func_3()", setup="from __main__ import func_3", number=100000))

print('func_4')
print(func_4())
print(timeit("func_4()", setup="from __main__ import func_4", number=100000))

"""
func_3 получилась самая быстра из-за смены списка на множество уникальных элементов массива.
Время - 0.251с
func_4 использует модуль numpy, её приемущество в лаконичности кода, хоть и работает она медленнее чем func_3,
но быстрее первых двух
Время - 0.659
"""
