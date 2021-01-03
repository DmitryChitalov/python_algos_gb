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


print(func_1())
print(func_2())

print(
    timeit(
        'func_1()',
        setup='from __main__ import func_1',
        number=10000
    )
)

print(
    timeit(
        'func_2()',
        setup='from __main__ import func_2',
        number=10000
    )
)


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def func_3():
    max_tuple = (0, array[0])
    for element in array:
        max_tuple = (array.count(element), element) if array.count(element) > max_tuple[0] else max_tuple
    return f'Чаще всего встречается число {max_tuple[1]}, ' \
           f'оно появилось в массиве {max_tuple[0]} раз(а)'


print(func_3())

print(
    timeit(
        'func_3()',
        setup='from __main__ import func_3',
        number=10000
    )
)


'''
При реализации программы третьим методом с применением мемоизации функции нахождения наиболее часто встречающегося
элемента в массиве (реализация через помещение в кортеж элемента и частоты его появления в массиве) получилось
сократить время исполнения программы относительно первых двух методов.'''