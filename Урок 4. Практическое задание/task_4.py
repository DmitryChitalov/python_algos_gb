"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

# Замеры при 100 повторов:
#
# ------------------------Вариант 1-----------------------------
# 0.0005908000000000024
# 0.04247490000000001
# 3.6526392
# ------------------------Вариант 2-----------------------------
# 0.0009386000000000116
# 0.03863489999999992
# 3.6472678
# ------------------------Вариант 3-----------------------------
# 0.0013269000000004638
# 0.0031232000000001037
# 0.025921699999999603


from timeit import timeit
from random import randint
from collections import Counter


# array = [1, 3, 1, 3, 4, 5, 1]


def new_random_arr(num):
    return [randint(i, num) for i in range(num)]


def func_1(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3(array):
    kw = Counter(array).most_common(1).pop()
    return f'Чаще всего встречается число {kw}, ' \
           f'оно появилось в массиве {kw} раз(а)'


if __name__ == '__main__':
    rep = 100
    arr_10 = new_random_arr(10)
    arr_100 = new_random_arr(100)
    arr_1000 = new_random_arr(1000)

    print('------------------------Вариант 1-----------------------------')
    print(
        timeit(
            "func_1(arr_10)",
            setup='from __main__ import func_1, arr_10',
            number=rep))
    print(
        timeit(
            "func_1(arr_100)",
            setup='from __main__ import func_1, arr_100',
            number=rep))
    print(
        timeit(
            "func_1(arr_1000)",
            setup='from __main__ import func_1, arr_1000',
            number=rep))

    print('------------------------Вариант 2-----------------------------')
    print(
        timeit(
            "func_2(arr_10)",
            setup='from __main__ import func_2, arr_10',
            number=rep))
    print(
        timeit(
            "func_2(arr_100)",
            setup='from __main__ import func_2, arr_100',
            number=rep))
    print(
        timeit(
            "func_2(arr_1000)",
            setup='from __main__ import func_2, arr_1000',
            number=rep))

    print('------------------------Вариант 3-----------------------------')
    print(
        timeit(
            "func_3(arr_10)",
            setup='from __main__ import func_3, arr_10',
            number=rep))
    print(
        timeit(
            "func_3(arr_100)",
            setup='from __main__ import func_3, arr_100',
            number=rep))
    print(
        timeit(
            "func_3(arr_1000)",
            setup='from __main__ import func_3, arr_1000',
            number=rep))
