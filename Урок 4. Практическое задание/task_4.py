"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import repeat
from random import randint

array = [randint(1, 150) for i in range(1000)]


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
    dict_for_count = {}
    for el in array:
        if el in dict_for_count:
            dict_for_count[el] += 1
        else:
            dict_for_count[el] = 1
    num_count = max(dict_for_count.values())
    max_num = max(dict_for_count, key=dict_for_count.get)
    return f'Чаще всего встречается число {max_num}, ' \
           f'оно появилось в массиве {num_count} раз(а)'


print(func_1())
print(
    min(repeat(
        "func_1()",
        globals=globals(),
        repeat=3,
        number=100)))

print(func_2())
print(
    min(repeat(
        "func_2()",
        globals=globals(),
        repeat=3,
        number=100)))

print(func_3())
print(
    min(repeat(
        "func_3()",
        globals=globals(),
        repeat=3,
        number=100)))

"""Добавлена func_3, но она хорошо работает или для массивов, больших по размеру, на том массиве, что был в примере,
 она хуже первой. Быстрее она потому, что пробегает по массиву всего 1 раз"""
