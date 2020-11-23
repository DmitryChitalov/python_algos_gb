"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
#
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


def my_func(*args):
    num = max(array, key=array.count)
    return(f'Число {num} встречается в массиву {array.count(num)} раза')


print(timeit.timeit('func_1()', setup='from __main__ import func_1', number=1000))
print(timeit.timeit('func_2()', setup='from __main__ import func_2', number=1000))
print(timeit.timeit('my_func()', setup='from __main__ import my_func', number=1000))
# print(func_2())


def my_func(*args):
    num = max(array, key=array.count)
    return(f'Число {num} встречается в массиву {array.count(num)} раза')


"""0.0024366000000000006
0.0034994999999999957
0.002649499999999999
Mission failed.
"""
