"""
Задание 1.
Приведен код, который позволяет сохранить в массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
Добавьте аналитику: что вы сделали и почему
"""
import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return (i for i in range(len(nums)) if nums[i] % 2 == 0)


nums = list(range(1000))
print("func_1", timeit.timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=1000), "millisecond")
print("func_2", timeit.timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=1000), "millisecond")
"""
Результат:
func_1 0.12260472500000001 millisecond
func_2 0.08689739599999999 millisecond

Обе функции имеют сложность O(n), но по времени вторая оптимизированная функция выполняется быстрее,
т.к. она реализована, через генератор, который работает быстрее, чем код с циклом for
"""