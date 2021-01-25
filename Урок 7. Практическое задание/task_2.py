"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import random


def merge_sort(sample):
    if len(sample) > 1:
        center = len(sample) // 2
        left = sample[:center]
        right = sample[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sample[k] = left[i]
                i += 1
            else:
                sample[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            sample[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            sample[k] = right[j]
            j += 1
            k += 1
        return sample


el = int(input('Введите число элементов: '))
sample = [random.uniform(0, 50) for _ in range(el)]
print('Исходный- ', sample)
print('Отсортированный- ', merge_sort(sample))
