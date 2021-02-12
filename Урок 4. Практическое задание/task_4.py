"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
"""
Чаще всего встречается число 722, оно появилось в массиве 23 раз(а)
Чаще всего встречается число 722, оно появилось в массиве 23 раз(а)
Чаще всего встречается число 722, оно появилось в массиве 23 раз(а)
Чаще всего встречается число 722, оно появилось в массиве 23 раз(а)
1.4934871999999997
1.4916858
0.14876630000000013
1.4880988999999998
Наиболее быстрым оказалось решение с созданием множества из массива,
так как в среднем, если в массиве есть повторяющиеся элементы, значительно
уменьшается количетво переборов - нет необходимости перебирать массив для
каждого элемента.
Однако, в случае если в массиве повторяющиеся элементы отсутствуют,
такой способ не даст выигрыша.
"""
from timeit import timeit
from collections import Counter
from random import randint


# array = [1, 3, 1, 3, 4, 5, 1]


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
    nums = set(array)
    num = 0
    total = 0
    for k in nums:
        count = array.count(k)
        if count > total:
            total = count
            num = k
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {total} раз(а)'


def func_4():
    num = max(array, key=array.count)
    total = array.count(num)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {total} раз(а)'


array = []
for i in range(10000):
    array.append(randint(0, 1000))

print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(
    timeit(
        "func_1()",
        setup='from __main__ import func_1',
        number=1))
print(
    timeit(
        "func_2()",
        setup='from __main__ import func_2',
        number=1))
print(
    timeit(
        "func_3()",
        setup='from __main__ import func_3',
        number=1))
print(
    timeit(
        "func_4()",
        setup='from __main__ import func_4',
        number=1))
