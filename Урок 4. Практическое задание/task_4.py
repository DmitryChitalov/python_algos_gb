"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

from collections import Counter
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

def my_func_1():
    count = Counter(array).most_common(1)
    return f'Чаще всего встречается число {count[0][0]}, ' \
           f'оно появилось в массиве {count[0][1]} раз(а)'

def my_func_2():
    max_numb = max(set(array), key=array.count)
    count = array.count(max_numb)
    return f'Чаще всего встречается число {max_numb}, ' \
           f'оно появилось в массиве {count} раз(а)'

print(f'{func_1.__name__}: {func_1()}')
print(timeit(
        'func_1()',
        setup='from __main__ import func_1',
        number=10000))

print(f'{func_2.__name__}: {func_2()}')
print(timeit(
        'func_2()',
        setup='from __main__ import func_2',
        number=10000))

print(f'{my_func_1.__name__}: {my_func_1()}')
print(timeit(
        'my_func_1()',
        setup='from __main__ import my_func_1',
        number=10000))

print(f'{my_func_2.__name__}: {my_func_2()}')
print(timeit(
        'my_func_2()',
        setup='from __main__ import my_func_2',
        number=10000))

"""
    Наиболее эффективным, с точки зрения времени исполнения является
    реализация алгоритма с помощью встроенных функций, который применен
    в функции {my_func_2} O(n):
    
*************************************************************************
*   D:/Stydy/GeekBrain/Python_2/Lesson_4/les_4-task-4.py                *
*   Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)    *
*   0.013732000000000001                                                *
*   Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)    *
*   0.0203828                                                           *
*   Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)    *
*   0.0364757                                                           *
*   Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)    *
*   0.013342599999999996                                                *
*************************************************************************
"""
