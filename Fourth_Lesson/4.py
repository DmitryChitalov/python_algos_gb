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


def my_func():
    max = 0
    elem = 0
    for el in set(array):
        if array.count(el) >= max:
            max = array.count(el)
            elem = el

    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max} раз(а)'

print(func_1())
print(func_2())
print(my_func())

print(timeit("func_1()",setup= "from __main__ import func_1",number=100000))
print(timeit("func_2()",setup= "from __main__ import func_2",number=100000))
print(timeit("my_func()",setup= "from __main__ import my_func",number=100000))

"""Результаты работы:

Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
0.247911739     func_1
0.352347403     func_2
0.228108274     my_func

Написанная мной 3-я функция смогла ненамного ускорить время выполнения алгоритма
наверное из-за использования только уникальных значений множества,
 и их последующего использования для проверки в списке
"""


