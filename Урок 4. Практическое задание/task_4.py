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

# пытался написать 3-ю функцию (и множества использовал и тд), но быстрее всего получилось с list comprehension,
# это быстрее чем 2-й вариант, но всё равно медленнее чем цикл. Цикл очень быстрый (1-й вариант).


def func_3():
    new_array = [array.count(el) for el in array]
    max_3 = max(new_array)

    elem = array[new_array.index(max_3)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_3} раз(а)'

# делаем замеры
# 1-й вариант

print(
    timeit(
        "func_1()",
        setup='from __main__ import func_1',
        number=100000))

# 2-й вариант

print(
    timeit(
        "func_2()",
        setup='from __main__ import func_2',
        number=100000))

# 3-й вариант

print(
    timeit(
        "func_3()",
        setup='from __main__ import func_3',
        number=100000))

