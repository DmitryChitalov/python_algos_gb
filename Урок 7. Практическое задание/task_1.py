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

import numpy as np

###########################################################
min = -100
max = 100
nel = 5

def_randnums = list(np.random.randint(min, max, nel))

print(def_randnums)


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
        if stop_flag:
            break
        stop_flag = True
        for j in range(len(nums) - 1 - i):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                stop_flag = False
    return nums


###########################################################
test_randnums = def_randnums.copy()
res = classic_bubble(test_randnums)
print(f"classic_bubble: {res}")

test_randnums = test_randnums.copy()
res = ext_bubble(test_randnums)
print(f"ext_bubble: {res}")

print(res)
print(def_randnums)
