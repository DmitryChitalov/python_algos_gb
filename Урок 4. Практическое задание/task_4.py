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
           f'оно появилось в массиве {m} раз(а).'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а).'


# При замерах, данная реализация показывает разные результаты,
# например при number=100 и 1000000 она чуть уступает в скорости func_1().
# При number=1000 и 100000 func_3() немного быстрее чем func_1()
# Но по стилю, на мой взгляд, она бесспорно выигрывает=)
def func_3():
    res = max(array, key=array.count)
    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {array.count(res)} раз(а).'


print(func_1(), 'Подсчет времени: ', timeit('func_1()', setup='from __main__ import func_1', number=1000000))
print(func_2(), 'Подсчет времени: ', timeit('func_2()', setup='from __main__ import func_2', number=1000000))
print(func_3(), 'Подсчет времени: ', timeit('func_3()', setup='from __main__ import func_3', number=1000000))
