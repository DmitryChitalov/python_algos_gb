"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr2 = [el for el in nums if el % 2 == 0]
    return new_arr2


n = [el for el in range(100)]
n1 = [el for el in range(1000)]
n2 = [el for el in range(10000)]
print(timeit("func_1(n)", globals=globals(), number=1000))
print(timeit("func_2(n)", globals=globals(), number=1000))
print(timeit("func_1(n1)", globals=globals(), number=1000))
print(timeit("func_2(n1)", globals=globals(), number=1000))
print(timeit("func_1(n2)", globals=globals(), number=1000))
print(timeit("func_2(n2)", globals=globals(), number=1000))

'''
так как генератор списка более оптимизирован, то по времени он выигрывает
 у цикла из первой функции.
*** при n = 100 и numbers = 1000:
  func_1 = 0.0098955
  func_2 = 0.0054963999999999985
*** при n = 1000 и numbers = 1000:
  func_1 = 0.1045964
  func_2 = 0.05171040000000002
*** при n = 10000 и numbers = 1000:
  func_1 = 1.0586513
  func_2 = 0.47981319999999994
'''