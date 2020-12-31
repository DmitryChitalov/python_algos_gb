"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""


import timeit


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
    array_count = [array.count(el) for el in array]
    max_count = max(array_count)
    max_count_elem = array[array_count.index(max_count)]
    return f'Чаще всего встречается число {max_count_elem}, ' \
           f'оно появилось в массиве {max_count} раз(а)'

print(func_1())
print(max(timeit.repeat('func_1()', "from __main__ import func_1", repeat=10, number=1000)))
print(func_2())
print(max(timeit.repeat('func_2()', "from __main__ import func_2", repeat=10, number=1000)))
print(func_3())
print(max(timeit.repeat('func_3()', "from __main__ import func_3", repeat=10, number=1000)))


# Добавил func_3, которая быстрее остальных за счет использования генератора списков
#
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# 0.005888600000000001
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# 0.005440299999999995
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# 0.004370700000000005
