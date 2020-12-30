"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

import timeit

array = [2, 2,3, 4, 1, 5, 2, 4, 7, 8, 9]


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
    new_array = [array.count(el) for el in array]

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'
    return new_array


def func_4():
    from collections import Counter
    return Counter(array).most_common()[0]


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(timeit.timeit("func_1", setup='from __main__ import func_1'))
print(timeit.timeit("func_2", setup='from __main__ import func_2'))
print(timeit.timeit("func_3", setup='from __main__ import func_3'))
print(timeit.timeit("func_4", setup='from __main__ import func_4'))

""" моя функция иногда быстрее иногда медленнее чем вторая функция, и 4 тая функция также"""