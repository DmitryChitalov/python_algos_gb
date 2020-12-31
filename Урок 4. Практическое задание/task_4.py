"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

1 Сделайте профилировку каждого алгоритма через timeit

2 Попытайтесь написать третью версию, которая будет самой быстрой.
3 Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

from timeit import timeit


array = [1, 3, 9, 7, 3,  7, 3, 5, 1, 3, 4, 5, 1, 3]


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

print(timeit('func_1', setup='from __main__ import func_1', number=1000), 'func_1')
print(timeit('func_2', setup='from __main__ import func_2', number=1000), 'func_2')


"""
2. попытаемся найти более быстрое решение.
попробем испльзовать встроенные функции max, set и метод .count()
"""


def my_func(lst):
    most_elem = max(set(lst), key=lst.count)
    amount_elem = lst.count(most_elem)
    return f'Чаще всего встречается число {most_elem}, оно встерчается {amount_elem} раз(а)'


print('my_func')
print(my_func(array))
print(timeit('my_func', setup='from __main__ import my_func, array', number=1000))

"""
Результат:
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
1.3600000000002499e-05 func_1
1.3200000000004875e-05 func_2
my_func
Чаще всего встречается число 1, оно встерчается 3 раз(а)
1.3100000000001999e-05
Как видим, my_func работает быстрее, т.к. используются встроенные функции,
хотя нужно признать, что результат неоднозначный, иногда при запуске программы my_func срабатывает медленнее
"""