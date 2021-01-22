"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import random
from timeit import timeit

numbers = [random.randint(-100, 100) for _ in range(10)]


def bubble_reverse(nums):  # Вариант №1
    for j in range(len(nums) - 1):
        for i in range(len(nums) - 1 - j):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


def bubble_reverse_upd(nums):  # Вариант №2
    n = 1
    k = True
    while n < len(nums):
        for i in range(len(nums)-n):
            if nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                k = False
        if k:
            break
        n += 1
    return nums


print('Исходный массив:', numbers)
print('Обратная пузырьковая:', bubble_reverse(numbers[:]))
print('Обратная пузырьковая:', bubble_reverse_upd(numbers[:]))
print(timeit('bubble_reverse(numbers[:])', 'from __main__ import bubble_reverse, numbers', number=1000))
print(timeit('bubble_reverse_upd(numbers[:])', 'from __main__ import bubble_reverse_upd, numbers', number=1000))

'''
Замеры на 1000 пробегов
Вариант №1 - 0.022974300000000003
Вариант №2 - 0.024516800000000005

Вариант №1 в оптимизации не нуждается.
'''