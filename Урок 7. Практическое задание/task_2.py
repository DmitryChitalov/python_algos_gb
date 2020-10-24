"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import random
from timeit import timeit


def merge_sort(in_list):
    if len(in_list) > 1:
        center = len(in_list) // 2
        left = in_list[:center]
        right = in_list[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                in_list[k] = left[i]
                i += 1
            else:
                in_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            in_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            in_list[k] = right[j]
            j += 1
            k += 1

        return in_list


if __name__ == '__main__':
    amount = int(input("Введите число элементов: "))
    random_list = [50 * random() for _ in range(amount)]
    print(f'Исходный массив: {random_list}\nОтсортированный массив: {merge_sort(random_list)}')
    print(f'Время выполнения функции: '
          f'{timeit(f"merge_sort({random_list[:]})", setup="from __main__ import merge_sort, random_list", number=1000)}')
