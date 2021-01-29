"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit
from statistics import mode

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
    return f'Чаще всего встречается число {mode(array)}, ' \
           f'оно  появилось в массиве {array.count(mode(array))} раз(а)'

def func_4():
    return  f'Чаще всего встречается число {max(array, key=array.count)}, ' \
           f'оно  появилось в массиве {array.count(max(array))} раз(а)'

print(func_1(), timeit('func_1()', globals=globals(), number=10000))
print(func_2(), timeit('func_2()', globals=globals(), number=10000))
print(func_3(), timeit('func_3()', globals=globals(), number=10000))
print(func_4(), timeit('func_4()', globals=globals(), number=10000))

"""
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а) 0.038691578000000004
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а) 0.04008500699999999
Чаще всего встречается число 1, оно  появилось в массиве 3 раз(а) 0.12223102499999997
Чаще всего встречается число 1, оно  появилось в массиве 1 раз(а) 0.03583889899999998

Наиболее быстрый вариант через функцию "max".
"""