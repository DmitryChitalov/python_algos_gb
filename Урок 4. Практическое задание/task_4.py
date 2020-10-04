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


def func_3():
    """ Версия медленнее func_1, но быстрее func_2, это максимум что у меня получился из 7 придуманных вариантов """
    result = [0]
    set_array = set(array)
    for i in set_array:
        if array.count(i) > result[0]:
            result = [array.count(i), i]
    return f'Чаще всего встречается число {result[1]}, ' \
           f'оно появилось в массиве {result[0]} раз(а)'


def func_4():
    """ В текущей вариации данное решениеи на 3ем месте по скорости,
    но оно становися самым быстрым при увеличении кол-ва элементов в массиве """
    num = max(set(array), key=array.count)
    cnt = array.count(num)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {cnt} раз(а)'


print(func_1(), timeit('func_1()', setup='from __main__ import func_1', number=1_000))
print(func_2(), timeit('func_2()', setup='from __main__ import func_2', number=1_000))
print(func_3(), timeit('func_3()', setup='from __main__ import func_3', number=1_000))
print(func_4(), timeit('func_4()', setup='from __main__ import func_4', number=1_000))
