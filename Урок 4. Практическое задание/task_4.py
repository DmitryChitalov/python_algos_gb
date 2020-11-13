"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import timeit

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
    new_array = set(array)
    m = 0
    num = 0
    for i in new_array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_4(array):
    return max(array, key=array.count)


print(timeit.timeit("func_1()", setup="from __main__ import func_1", number=100000))
print(timeit.timeit("func_2()", setup="from __main__ import func_2", number=100000))
print(timeit.timeit("func_3()", setup="from __main__ import func_3", number=100000))
print(timeit.timeit("func_4(array)", setup="from __main__ import func_4, array", number=100000))


'''Самый эффективный вариант - использование встроенных функций, как в последнем решении.
Почти не уступает вариант поиска по циклу с приведением списка к множеству для выделения уникальных
элементов и сокращения работы в цикле.'''