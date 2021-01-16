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


print(func_1())
print(func_2())

def func_3():
    number = max(array, key=array.count)
    return f'Чаще всего встречается число {number}, ' \
           f'оно появилось в массиве {array.count(number)} раз(а)'
print(func_3())

print(
    timeit(
        "func_1()",
        setup='from __main__ import func_1',
        number=10000))
print('func_1')
print(
    timeit(
        "func_2()",
        setup='from __main__ import func_2',
        number=10000))
print('func_2')
print(
    timeit(
        "func_3()",
        setup='from __main__ import func_3',
        number=10000))
print('func_3')

"""
Результаты замеров при 10000 повторениях
0.022256900000000003
func_1
0.0280085
func_2
0.0202957
func_3
"""