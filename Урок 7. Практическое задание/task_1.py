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

from random import randint
from timeit import timeit


def print_timeint(func_name, n):
    print(f'{func_name} {timeit(f"{func_name}({n})", globals=globals(), number=10000)}')


my_list = [randint(-100, 100) for el in range(100)]


def buble_sort_simple(l):
    length = len(l)
    for i in range(length):
        for j in range(0, length - i - 1):
            if l[j] > l[j + 1]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
    return l


def buble_sort_optimized(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return nums


def supper_bubble(l):
    return sorted(l)


print_timeint('buble_sort_optimized', my_list)

print_timeint('buble_sort_simple', my_list)

print_timeint('supper_bubble', my_list)

"""
buble_sort_optimized 11.3699528
buble_sort_simple 6.796275999999999
supper_bubble 0.03271040000000269

Стандартный вариант сортировки эффективнее чем с прерыванием. Но лучше всех показала себя встренная функция sorted


"""
