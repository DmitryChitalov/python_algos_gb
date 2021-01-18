"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

from timeit import timeit, default_timer, Timer, repeat
from collections import Counter


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
    return sorted([[i, array.count(i)] for i in set(array)], key=lambda t: t[1])[-1]


def func_4():
    return Counter(array).most_common(1)


t1 = Timer("func_1()", "from __main__ import func_1")
print(t1.timeit(number=1000))
print(timeit("func_2()", "from __main__ import func_2", number=1000))
print(repeat("func_3()", "from __main__ import func_3", default_timer, 3, 1000))
print(repeat("func_4()", "from __main__ import func_4", default_timer, 3, 1000))


print(func_1())
print(func_2())


"""
Написал две другие функции, находящие самое часто встречаемое число, первая в одну строку
с методом sorted, list comprehension и lambda-выражением. Вторая через класс Counter 
и метод most_common модуля collections, но ни одна не получилась быстрее func_2
"""