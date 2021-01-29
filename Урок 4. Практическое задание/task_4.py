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
    res = [array.count(i) for i in array]
    max_count = max(res)
    elem = array[res.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_count} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(timeit("func_1", setup="from __main__ import func_1", number=1000))
print(timeit("func_2", setup="from __main__ import func_1", number=1000))
print(timeit("func_3", setup="from __main__ import func_1", number=1000))

# Особо ускорить не получилось, но код выглядит почище.
# Ускорить не получилось, так как все решения используют встроенную функцию count(), которая считает количество
# повторений элемента в списке, что есть самое быстрое решение подсчета элементов в списке.
# Далее, есть варианты: можно вести счетчики (func_1), а можно сохранять значения в новом списке
# (это более затратно по памяти). Но существенно, кажется, мы мало что здесь выиграем.


