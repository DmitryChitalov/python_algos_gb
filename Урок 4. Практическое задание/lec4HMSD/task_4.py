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
    new_array = {}
    k = 0
    res = ""
    for el in array:
        if new_array.get(el):
            new_array[el] = int(new_array.get(el))+1
            if new_array.get(el)>k:
                k = new_array.get(el)
                res = el
        else:
            new_array[el] = 1


#   k = 0
#    res = ""
#    for el in new_array:
#        if new_array.get(el)>k:
#            k = new_array.get(el)
#            res = el

    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {k} раз(а)'

def func_4():
    res = max(array, key = array.count)
    k = array.count(res)

    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {k} раз(а)'

def func_5():
    res = max(array, key=array.count)
    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {array.count(res)} раз(а)'

print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())

print(
    timeit(
        'func_1()',
        setup='from __main__ import func_1',
        number=100000))

print(
    timeit(
        'func_2()',
        setup='from __main__ import func_2',
        number=100000))

print(
    timeit(
        'func_3()',
        setup='from __main__ import func_3',
        number=100000))

print(
    timeit(
        'func_4()',
        setup='from __main__ import func_4',
        number=100000))

print(
    timeit(
        'func_5()',
        setup='from __main__ import func_5',
        number=100000))

#0.40592439999999996
#0.5877918
#0.5486405000000001
#0.4217312999999998
#0.4122962000000001

#Используя встроенные функции, в версии 4 позволили незначительно ускорить работу. Вариант через словарь потерпел неудачу, хотя он оказался быстрее
#ВАриант в 5й функции без временной переменной, при расчете сразу в return оказался также незначительно быстрее.