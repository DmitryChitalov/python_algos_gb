"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

from cProfile import run
from random import randint

# array = [1, 3, 1, 3, 4, 5, 1]

array = [randint(0, 10) for i in range(10000)]



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
    result = max(array, key=array.count)
    return f'Чаще всего встречается число {result}, оно появилось ' \
           f'в массиве {array.count(result)} раз'


def func_4():
    arr_set = set(array)
    elem = None
    elem_count = 0
    for i in arr_set:
        el = array.count(i)
        if el > elem_count:
            elem_count = el
            elem = i
    return f'Чаще всего встречается число {elem}, оно появилось ' \
           f'в массиве {elem_count} раз'


print(func_1())
print(func_2())
print(func_3())
print(func_4())


def main():
    res_count = func_1()
    res_count_2 = func_2()
    res_count_3 = func_3()
    res_count_4 = func_4()


run('main()')

# задачу ускорить получилось с помощью встроенной фукнкции max,
# а так же простым перебором без копирования списка

"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.213    3.213 <string>:1(<module>)
        1    0.002    0.002    1.065    1.065 task_4.py:22(func_1)
        1    0.003    0.003    1.067    1.067 task_4.py:34(func_2)
        1    0.000    0.000    1.079    1.079 task_4.py:46(func_3)
        1    0.000    0.000    0.001    0.001 task_4.py:52(func_4)
"""
