"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""


from timeit import timeit

test_arr = [1, 3, 1, 3, 4, 5, 1, 3, 3, 3]


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
    return max(array, key=array.count)


print(func_1(test_arr))
print(func_2(test_arr))
print(func_3(test_arr))

print(timeit('func_1(test_arr)',
             'from __main__ import func_1, test_arr', number=100000))

print(timeit('func_2(test_arr)',
             'from __main__ import func_2, test_arr', number=100000))

print(timeit('func_3(test_arr)',
             'from __main__ import func_3, test_arr', number=100000))

"""
Вывод - реализация через встроенную функцию max быстрее всего
"""
