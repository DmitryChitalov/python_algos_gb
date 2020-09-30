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


def func_2(nums):
    """ решение через генератор списка """
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_3(nums):
    """ решение через генератор """
    new_arr_gen = (i for i in range(len(nums)) if nums[i] % 2 == 0)
    return new_arr_gen


nums = [1, 2, 3, 4, 5, 6, 7, 8]
print("\nTest 1 - 1")
print(timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=1))  # -> 8.41e-06   9.39e-06
print(timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=1))  # -> 5.35e-06   6.88e-06
print(timeit("func_3(nums)", setup="from __main__ import func_3, nums", number=1))  # -> 4.59e-06   4.59e-06

print("\nTest 2 - 1_000")
print(timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=1_000))  # -> 0.0021    0.0026
print(timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=1_000))  # -> 0.0025    0.0028
print(timeit("func_3(nums)", setup="from __main__ import func_3, nums", number=1_000))  # -> 0.0014    0.0015

print("\nTest 2 - 1_000_000")
print(timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=1_000_000))  # -> 2.24   2.20
print(timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=1_000_000))  # -> 2.69   2.29
print(timeit("func_3(nums)", setup="from __main__ import func_3, nums", number=1_000_000))  # -> 1.41   1.24

""" Выводы:
    Приведённый пример имеет линейную сложность(цикл), решение через генератор списков тоже линейное, но запись
    локаничнее. При маленьком кол-ве запусков генератор списка срабатыввает быстрее цикла, а с ростом кол-ва запусков
    генератор списка срабатывает дольше. Но во всех случаях и тем более при увеличении кол-ва запусков быстрее всех
    работает генератор. Это обусловлено отсутствием ожидания рендеринга всех значений и генератор не занимает память
    под все элементы, только под 1 в каждый момент времени. Данное решение считаю самым лучшим.
"""

