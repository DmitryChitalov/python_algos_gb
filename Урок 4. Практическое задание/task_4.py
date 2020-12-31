"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

# Получилось усовершенствовать первый метод, он получился быстрее
# Я делала массив множеством(убрались повторы) - отсюда цикл получился укороченным,
# соответственно время уменьшилось (конечно, при отсутствии повторяющихся элементов, этот вариант не сработает:))


from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 5, 5, 1, 555, 654, 6, 6, 12, 13, 14, 5, 6, 8, 10, 7, 8, 8, 9]


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


print('Вариант 1')
print(timeit("func_1()", setup="from __main__ import func_1, array", number=1000))


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print('Вариант 2')
print(timeit("func_2()", setup="from __main__ import func_2, array", number=1000))


def func_3():
    m = 0
    v = 0
    new = set(array)
    for i in new:
        count = array.count(i)
        if count > m:
            m = count
            v = i
    return f'Чаще всего встречается число {v}, ' \
           f'оно появилось в массиве {m} раз(а)'


print('Вариант 3')
print(timeit("func_3()", setup="from __main__ import func_3, array", number=1000))

print(func_1())
print(func_2())
print(func_3())
