"""
Задание 4.

Приведены два алгоритма. В них определяется число, которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""


import random
from timeit import timeit


array = [random.randint(0, 10) for el in range(10)]


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
    return f'Чаще всего встречается число {elem}, оно появилось в массиве {max_2} раз(а)'


def func_3():
    numb = max(array, key=array.count)
    return f"Чаще всего встречается число {numb}, оно появилось в массиве {array.count(numb)} раз(а)"


print(func_1())
print(func_2())
print(func_3())

print(timeit("func_1()", setup="from __main__ import func_1"))
print(timeit("func_2()", setup="from __main__ import func_2"))
print(timeit("func_3()", setup="from __main__ import func_3"))



"""По сути 3й способ должен был ускорить выполнение операции, но при выполнении замеров, опытным путём получилось, что самый быстрый способ -- первый."""