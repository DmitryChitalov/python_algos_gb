"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

import timeit
from statistics import mode
import cProfile

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
    elem = max(set(array), key = array.count)
    max_3 = array.count(elem)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_3} раз(а)'


def func_4():
    elem = (mode(array))
    max_4 = array.count(elem)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_4} раз(а)'

def main():
    func_1()
    func_2()
    func_3()
    func_4()


print(timeit.timeit("func_1()", setup="from __main__ import func_1"))
print(timeit.timeit("func_2()", setup="from __main__ import func_2"))
print(timeit.timeit("func_3()", setup="from __main__ import func_3"))
print(timeit.timeit("func_4()", setup="from __main__ import func_4"))

cProfile.run('main()')

#
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 __init__.py:540(__init__)
   #      1    0.000    0.000    0.000    0.000 __init__.py:559(most_common)
   #      1    0.000    0.000    0.000    0.000 __init__.py:608(update)
   #      6    0.000    0.000    0.000    0.000 _collections_abc.py:392(__subclasshook__)
   #    6/1    0.000    0.000    0.000    0.000 abc.py:100(__subclasscheck__)
   #      1    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
   #      1    0.000    0.000    0.000    0.000 hW_4_task_4.py:19(func_1)
   #      1    0.000    0.000    0.000    0.000 hW_4_task_4.py:31(func_2)
   #      1    0.000    0.000    0.000    0.000 hW_4_task_4.py:43(func_3)
   #      1    0.000    0.000    0.000    0.000 hW_4_task_4.py:50(func_4)
   #      1    0.000    0.000    0.000    0.000 hW_4_task_4.py:56(main)
   #      1    0.000    0.000    0.000    0.000 heapq.py:521(nlargest)
   #      1    0.000    0.000    0.000    0.000 statistics.py:534(mode)
   #      1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
   #    6/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
   #      1    0.000    0.000    0.000    0.000 {built-in method _collections._count_elements}
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
   #      2    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
   #      3    0.000    0.000    0.000    0.000 {built-in method builtins.max}
   #      7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
   #     16    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
# Ускорить получилось