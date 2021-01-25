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
    my_dict = {i: array.count(i) for i in array}
    my_dict = sorted(my_dict.items(), key=lambda val: val[1])
    elem = my_dict.pop()
    return f'Чаще всего встречается число {elem[0]}, ' \
           f'оно появилось в массиве {elem[1]} раз(а)'


def func_4():
    number = max(array, key=array.count)
    return f'Чаще всего встречается число {number}, ' \
           f'оно появилось в массиве {array.count(number)} раз(а)'


print(func_1())
print('Первая функция', timeit('func_1()', setup='from __main__ import func_1, array', number=100000))
print(func_2())
print('Вторая функция', timeit('func_2()', setup='from __main__ import func_2, array', number=100000))
print(func_3())
print('Третья функция', timeit('func_3()', setup='from __main__ import func_3, array', number=100000))
print(func_4())
print('Четвертая функция', timeit('func_4()', setup='from __main__ import func_4, array', number=100000))

"""
Оптимизировать код получилось, ускорить задачу не получилось. 
Первая функция 0.17021151499999998
Вторая функция 0.222199595
Третья функция 0.295378086
Четвертая функция 0.17292247699999996
"""