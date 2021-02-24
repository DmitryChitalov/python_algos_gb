"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""

import random
import collections
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1, 234, 234, 234, 234, 234, 234, 234,234, 234, 234, 234, 234, 234, 234,
         1, 3, 1, 3, 4, 5, 1, 234, 234, 234, 234, 234, 234, 234,234, 234, 234, 234, 234, 234, 234,
         1, 3, 1, 3, 4, 5, 1, 234, 234, 234, 234, 234, 234, 234,234, 234, 234, 234, 234, 234, 234,
         1, 3, 1, 3, 4, 5, 1, 234, 234, 234, 234, 234, 234, 234,234, 234, 234, 234, 234, 234, 234,
         1, 3, 1, 3, 4, 5, 1, 234, 234, 234, 234, 234, 234, 234,234, 234, 234, 234, 234, 234, 234,
         1, 3, 1, 3, 4, 5, 1, 234, 234, 234, 234, 234, 234, 234,234, 234, 234, 234, 234, 234, 234,
         1, 3, 1, 3, 4, 5, 1, 234, 234, 234, 234, 234, 234, 234,234, 234, 234, 234, 234, 234, 234,]


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


print(func_1())
print(func_2())

# -----------------------------------------------------


def func_3():
    numb = max(array, key=array.count)
    return f'Чаще всего встречается число {numb}, ' \
           f'оно появилось в массиве {array.count(numb)} раз(а)'


def func_4():
    unique_info = collections.defaultdict(int)
    max_key = None
    max_value = 0
    for key in array:
        unique_info[key] += 1
        value = unique_info[key]
        if value > max_value:
            max_value = value
            max_key = key
    return f'Чаще всего встречается число {max_key}, ' \
           f'оно появилось в массиве {max_value} раз(а)'


print(func_3())
print(func_4())
print(timeit("func_1()", globals=globals(), number=10000))
print(timeit("func_2()", globals=globals(), number=10000))
print(timeit("func_3()", globals=globals(), number=10000))
print(timeit("func_4()", globals=globals(), number=10000))

"""
Вывод:
все результаты с функцией count (func_1, func_2, func_3) на более менее больших 
массивах недопустимо медленны в плане скорости (уже от 20 элементов при 10000 повторах)
(в этом примере использовался массив из 147 элементов и 10000 повторов) вариант через словарь ГОРАЗДО быстрее:

func_1(count):            3.0916749
func_2(count):            3.0880875000000003
func_3(count):            2.7705677
func_4(словарь):          0.3870730999999985

"""
