"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

from timeit import timeit
import random
import numpy as np

###########################################################
min = -1000
max = 1000
nel = 5000

#def_randnums = list(np.random.randint(min, max, nel))
def_randnums = [random.randint(min, max) for _ in range(nel)]


# def_randnums = []
# def_randnums.extend(range(nel, 1, -1))
# def_randnums.extend(range(1, nel, 1))

# print(def_randnums)


###########################################################
def classic_bubble(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


###########################################################
def ext_bubble(nums):
    stop_flag = False

    for i in range(len(nums)):
        if stop_flag == True:
            return nums
        stop_flag = True
        for j in range(len(nums) - 1 - i):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                stop_flag = False
    return nums


###########################################################
def list_sort_s(nums):
    return sorted(nums, key=int, reverse=True)


###########################################################
n_iter = 50
###########################################################
test_randnums = def_randnums.copy()
res = classic_bubble(test_randnums)
test_randnums = def_randnums.copy()
print(
    timeit(
        f"classic_bubble: test_randnums",
        setup=f'from __main__ import classic_bubble, test_randnums',
        number=n_iter))

###########################################################

test_randnums = def_randnums.copy()
res = ext_bubble(test_randnums)
test_randnums = def_randnums.copy()
print(
    timeit(
        f"ext_bubble: test_randnums",
        setup=f'from __main__ import ext_bubble, test_randnums',
        number=n_iter))

###########################################################

test_randnums = def_randnums.copy()
res = list_sort_s(test_randnums)
test_randnums = def_randnums.copy()
print(
    timeit(
        f"list_sort_s: test_randnums",
        setup=f'from __main__ import list_sort_s, test_randnums',
        number=n_iter))

###########################################################

'''

1.132000000403366e-06
1.1329999995979279e-06
7.560000003792311e-07

На больших размерах у меня комп зависает.
Видно что улучшеный пузырёк лучше классического.
Но всторенный sort работает быстрее.

'''