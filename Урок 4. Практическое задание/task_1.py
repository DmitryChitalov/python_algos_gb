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


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2_generator(nums):
    return [i for i, j in enumerate(nums) if j % 2 == 0]


nums_test = [el for el in range(10000)]

t_1 = Timer("func_1(nums_test)", 'from __main__ import func_1, nums_test')
print('func_1', t_1.timeit(number=1000), 'ms')

t_2 = Timer("func_2_generator(nums_test)", 'from __main__ import func_2_generator, nums_test')
print('func_2_generator', t_2.timeit(number=1000), 'ms')

# Генератор ускоряет создание нового списка, а функция enumerate позволяет получить индекс текущего элемента, если
# элемент подходит по условию.
#
# func_1 2.3106074 ms
# func_2_generator 1.6419603000000005 ms
