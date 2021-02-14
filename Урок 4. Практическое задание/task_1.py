"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

"""
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры
Добавьте аналитику: что вы сделали и почему
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""

from timeit import timeit


STR_CODE_1 = '''
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
def fill_list():
    for i in range(10000):
        nums_list.append(i)
nums_list = list()
fill_list()
func_1(nums_list)
'''

STR_CODE_2 = '''
def func_2(nums):
    new_arr_2 = []
    for i in range(0,len(nums),2):
        new_arr_2.append(i)
    return new_arr_2
def fill_list():
    for i in range(10000):
        nums_list.append(i)
nums_list = list()
fill_list()
func_2(nums_list)
'''

max_iter = 10000  # количество повторов для измерения
print("func_1 ", timeit(STR_CODE_1, number=max_iter))
print("func_2 ", timeit(STR_CODE_2, number=max_iter))

"""
В первом случае осувщесвляется выбор элемента по индексу, потом проверка его четности с помощью деления на 2.
Во втором сразу берем каждый 2 индекс, начиная с 0
Это работает быстрее, т.к нет самой операции деления индекса.
"""