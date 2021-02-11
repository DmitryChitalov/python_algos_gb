"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

from timeit import timeit
from random import randint

array = [1, 3, 1, 3, 4, 5, 1]
#array = [randint(1, 10) for i in range(100)]


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


def my_func():
    max_numb = max(set(array), key=array.count)
    count = array.count(max_numb)
    return f'Чаще всего встречается число {max_numb}, ' \
           f'оно появилось в массиве {count} раз(а)'


print(timeit(
        'func_1()',
        setup='from __main__ import func_1',
        number=10000))
print(timeit(
        'func_2()',
        setup='from __main__ import func_2',
        number=10000))
print(timeit(
        'my_func()',
        setup='from __main__ import my_func',
        number=10000))

"""
Со списком по умолчанию выигрыша по времени выполнения не получается, все три функции
дают сопоставимые числа. Но если применять функции к большим спискам (в примере на 100 элементов)
скорость выполнения вырастает на порядок
"""
