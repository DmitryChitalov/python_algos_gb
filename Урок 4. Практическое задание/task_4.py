"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

import timeit
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 1]


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
    max_3 = max(set(array), key = array.count)
    return f'Чаще всего встречается число {max_3}, ' \
           f'оно появилось в массиве {array.count(max_3)} раз(а)'



print(func_1())
print(func_2())
print(func_3())


print(timeit.timeit("func_1()", setup="from __main__ import func_1"))
print(timeit.timeit("func_2()", setup="from __main__ import func_2"))
print(timeit.timeit("func_3()", setup="from __main__ import func_3"))

"""
func_1: 2.2708536
func_2: 2.6721615
func_3: 1.8042268999999997
Ускорить выполнение задачи удалось за счет преобразования в множество с уникальными значениями, 
и использования встроеной функции max с параметрами.
"""