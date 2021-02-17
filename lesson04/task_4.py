"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
from random import randint
from timeit import repeat

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

def my_func():
    result = max((array.count(element), element) for element in array)
    return f'Чаще всего встречается число {result[1]}, ' \
           f'оно появилось в массиве {result[0]} раз(а)'


# print(func_1())
# print(func_2())
# print(my_func())

print(f"func_1 n=5", end=' ')
print(repeat("func_1()", repeat = 3, number=100000, globals=globals()))
print(f"func_2 n=5", end=' ')
print(repeat("func_2()", repeat = 3, number=100000, globals=globals()))
print(f"my_func n=5", end=' ')
print(repeat("my_func()", repeat = 3, number=100000, globals=globals()))

for arr_len in [100, 1000, 10000]:
    random_list = list(randint(0,100) for el in range(arr_len))
    print(f"func_1 n={arr_len}", end=' ')
    print(repeat("func_1()", repeat=3, number=100000, globals=globals()))
    print(f"func_2 n={arr_len}", end=' ')
    print(repeat("func_2()", repeat=3, number=100000, globals=globals()))
    print(f"my_func n={arr_len}", end=' ')
    print(repeat("my_func()", repeat=3, number=100000, globals=globals()))


# func_1 n=5 [0.2120264, 0.20751819999999999, 0.37212909999999993]
# func_2 n=5 [0.2656109000000001, 0.30543070000000005, 0.44476650000000006]
# my_func n=5 [0.47140709999999975, 0.43172989999999967, 0.4284597999999997]
# func_1 n=100 [0.21684949999999992, 0.24348750000000008, 0.25027829999999973]
# func_2 n=100 [0.3118582999999999, 0.2984252000000005, 0.26559820000000034]
# my_func n=100 [0.3160654000000003, 0.3390409999999999, 0.34747720000000015]
# func_1 n=1000 [0.21148770000000017, 0.1768641999999998, 0.2323189999999995]
# func_2 n=1000 [0.3648150000000001, 0.2851816000000005, 0.24266889999999997]
# my_func n=1000 [0.2769718999999995, 0.33391660000000023, 0.3302839999999998]
# func_1 n=10000 [0.22697789999999962, 0.2204613000000002, 0.2000895000000007]
# func_2 n=10000 [0.26677070000000036, 0.25340269999999876, 0.2554362000000001]
# my_func n=10000 [0.30144729999999953, 0.30907020000000074, 0.3162807000000001]
#
# Мой лаконичный вариант оказывается самый медленный. Печаль.