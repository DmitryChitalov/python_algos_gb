"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 1]
#array = [1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3,
#         1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1]


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
    c = Counter(array)
    res = c.most_common(1)[0]
    return f'Чаще всего встречается число {res[0]}, ' \
           f'оно появилось в массиве {res[1]} раз(а)'


def func_4():
    res = max((array.count(i), i) for i in array)
    return f'Чаще всего встречается число {res[1]}, ' \
           f'оно появилось в массиве {res[0]} раз(а)'

print('С исходным списком')
print(f"func_1 {timeit('func_1()', number=10000, globals=globals())}")
print(f"func_2 {timeit('func_2()', number=10000, globals=globals())}")
print(f"func_3 {timeit('func_3()', number=10000, globals=globals())}")
print(f"func_4 {timeit('func_4()', number=10000, globals=globals())}")
array = [1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3,
         1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1]
print('С более большим списком')
print(f"func_1 {timeit('func_1()', number=10000, globals=globals())}")
print(f"func_2 {timeit('func_2()', number=10000, globals=globals())}")
print(f"func_3 {timeit('func_3()', number=10000, globals=globals())}")
print(f"func_4 {timeit('func_4()', number=10000, globals=globals())}")

"""
С исходным списком  выигрывают 1,2,4 функции
func_1 0.0163634
func_2 0.0212064
func_3 0.050328499999999984
func_4 0.021383600000000003
С более большим списком тут явный профит от Counter
func_1 0.30652959999999996
func_2 0.34609979999999996
func_3 0.04670249999999998
func_4 0.3426542

"""