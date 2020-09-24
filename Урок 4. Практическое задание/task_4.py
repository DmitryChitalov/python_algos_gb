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
    return f'func_1 = Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'func_2 - Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    index_list = [(array.count(x), x) for x in set(array)]
    elem = sorted(index_list)[-1][1]
    return f'func_3 - Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'


def func_4():
    new_array = sorted([(i, array.count(i)) for i in set(array)], key=lambda t: t[1])[-1]
    return f'func_4 - Чаще всего встречается число {new_array[0]}, ' \
           f'оно появилось в массиве {new_array[1]} раз(а)'


def func_5():
    a_set = set(array)
    most_common = None
    qty_most_common = 0
    for item in a_set:
        qty = array.count(item)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common = item
    return f'func_5 - Чаще всего встречается число {most_common}, ' \
           f'оно появилось в массиве {qty_most_common} раз(а)'


print(func_1())
print(timeit("func_1()", setup="from __main__ import func_1, array", number=1000))

print(func_2())
print(timeit("func_2()", setup="from __main__ import func_2, array", number=1000))

print(func_3())
print(timeit("func_3()", setup="from __main__ import func_3, array", number=1000))

print(func_4())
print(timeit("func_4()", setup="from __main__ import func_4, array", number=1000))

print(func_5())
print(timeit("func_5()", setup="from __main__ import func_5, array", number=1000))

"""Быстрее работает последняя функция за счет удаления повторяющихся элементов.
P.S. Последние две функции честно найдены в интернете. :)"""
