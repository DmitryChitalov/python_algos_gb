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
    new_array = [array.count(el) for el in array]

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_4():
    new_array = list(map(lambda el: array.count(el), array))

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(timeit("func_1()", setup='from __main__ import func_1', number=10000))
print(timeit("func_2()", setup='from __main__ import func_2', number=10000))
print(timeit("func_3()", setup='from __main__ import func_3', number=10000))
print(timeit("func_4()", setup='from __main__ import func_4', number=10000))

"""
Написал 2 дополнительных решения с использованием генераторного выражения, по скорости лучше чем 2-я ф-я и
с использованием ф-и map куда передал lambda + массив, но это оказалось самым медленным решением.
Ускорить быстрее чем ваша 1-я функция, мне не удалось, но 2-ю ускорил, за счет генераторного выражения.
"""

