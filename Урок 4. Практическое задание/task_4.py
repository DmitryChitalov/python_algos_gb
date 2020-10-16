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
    """
    Моя реализация нахождения самого частого числа в массиве.
    """
    res = max(array, key=array.count)
    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {array.count(res)} раз(а)'


print(func_1())
print(func_2())
print(func_3())

stmts = ('func_1', 'func_2', 'func_3')
for stmt in stmts:
    print(f'Алгоритм {stmt}:')
    print(timeit(f"{stmt}()",
                 setup=f'from __main__ import {stmt}',
                    number=10000))

"""
Профилировка ожидаемо показывает, что функция func_2 самая медленная из
трёх, т.к. имеет много лишних действий по созданию и обработке второго
массива.
"""