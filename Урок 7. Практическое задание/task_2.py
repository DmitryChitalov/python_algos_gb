"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from heapq import merge
from timeit import timeit
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


if __name__ == '__main__':
    a = int(input('Введите число элементов: '))
    b = [random.uniform(0, 50) for _ in range(a)]
    print('Исходный - ', b)
    print('Отсортированный - ', merge_sort(b))
    print('\nЗамеры на массивах разной длины:')
    print(timeit('merge_sort(c)', 'c = [random.uniform(0, 50) for _ in range(10)]', number=1, globals=globals()))
    print(timeit('merge_sort(c)', 'c = [random.uniform(0, 50) for _ in range(100)]', number=1, globals=globals()))
    print(timeit('merge_sort(c)', 'c = [random.uniform(0, 50) for _ in range(1000)]', number=1, globals=globals()))
