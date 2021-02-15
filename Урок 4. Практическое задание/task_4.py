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
    res = max((array.count(i), i) for i in array)
    return f'Чаще всего встречается число {res[1]}, ' \
           f'оно появилось в массиве {res[0]} раз(а)'


# array = [1, 3, 1, 3, 4, 5, 1]
array = [randint(0, 1000) for i in range(20)]

print(f"{timeit('func_1()', number=10000, globals=globals())}")
print(f"{timeit('func_2()', number=10000, globals=globals())}")
print(f"{timeit('my_func()', number=10000, globals=globals())}")

# Со списком в задании выигрывают функции 1,2. Но как только берем список больше, выигрывает мой вариант
