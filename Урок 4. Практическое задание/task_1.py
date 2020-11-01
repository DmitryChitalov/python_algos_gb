"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit, default_timer


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]    # O(n**2)


def func_3(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]      # O(n)


sample_nums = [0, 5, 8, 6, 10, 15, 17, 25, 30]

print(func_1(sample_nums))
print(f"func_1: {timeit('func_1(sample_nums)', 'from __main__ import func_1, sample_nums', default_timer)}")
# >>> func_1: 2.2304985

print(func_2(sample_nums))
print(f"func_2: {timeit('func_2(sample_nums)', 'from __main__ import func_2, sample_nums', default_timer)}")
# >>> func_2: 2.0351537

print(func_3(sample_nums))
print(f"func_3: {timeit('func_3(sample_nums)', 'from __main__ import func_3, sample_nums', default_timer)}")
# >>> func_3: 1.689384

"""
Для ускорения я убрал цикл for и вместо него использовал генераторное выражение с условием.
Причем в генераторном выражении (func_3) использовал встроенную функцию enumerate(),
которая позволяет извлекать сразу и индекс елемента и его значение, что значительно сокращает время,
т.к. нет необходимости обращаться к элементу массива по индексу - O(n) вместо O(n**2)
"""
