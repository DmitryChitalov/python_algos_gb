"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
from timeit import Timer


mass_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
          29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
          55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
          81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


def func_1():
    new_arr = []
    for i in range(len(mass_1)):
        if mass_1[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2():
    new_arr = [i for i in range(len(mass_1)) if mass_1[i] % 2 == 0]
    return new_arr


def func_3():
    new_arr = [v for k,v in enumerate(mass_1) if not k % 2]
    return new_arr


def func_4():
    new_arr = []
    for k,v in enumerate(mass_1):
        if not k % 2:
            new_arr.append(v)
    return new_arr


def func_5():
    new_arr = []
    for el in mass_1:
        if el % 2 == 0:
            new_arr.append(mass_1.index(el))
    return new_arr


def func_6():
    new_arr = [mass_1.index(el) for el in mass_1  if el % 2 == 0]
    return new_arr


def func_7():
    new_arr = list(v for k,v in enumerate(mass_1) if not k % 2)
    return new_arr


t_1 = Timer("func_1()", "from __main__ import func_1")
print("func_1 ", t_1.timeit(number=1000000), 'seconds')

t_2 = Timer("func_2()", "from __main__ import func_2")
print("func_2 ", t_2.timeit(number=1000000), 'seconds')

t_3 = Timer("func_3()", "from __main__ import func_3")
print("func_3 ", t_3.timeit(number=1000000), 'seconds')

t_4 = Timer("func_4()", "from __main__ import func_4")
print("func_4 ", t_4.timeit(number=1000000), 'seconds')

t_5 = Timer("func_5()", "from __main__ import func_5")
print("func_5 ", t_5.timeit(number=1000000), 'seconds')

t_6 = Timer("func_6()", "from __main__ import func_6")
print("func_6 ", t_6.timeit(number=1000000), 'seconds')

t_7 = Timer("func_7()", "from __main__ import func_7")
print("func_7 ", t_7.timeit(number=1000000), 'seconds')



# func_1  6.442846 milliseconds
# func_2  5.260066500000001 milliseconds
# func_3  4.414180100000001 milliseconds
# func_4  5.450349199999998 milliseconds
# func_5  30.974563100000005 milliseconds
# func_6  29.663503799999994 milliseconds
# func_7  5.53779209999999 milliseconds

# Сделал еще несколько вариантов функции. Самый быстрый вариант 3. Генераторное выражение + использование словаря