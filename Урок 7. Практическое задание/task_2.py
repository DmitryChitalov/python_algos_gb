"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import timeit
import random

def sl(a):
    if len(a) > 1:
        center = len(a) // 2
        left = a[:center]
        right = a[center:]

        sl(left)
        sl(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
        return a

n = int(input('Введите число элементов: '))
start_list = [random.uniform(0, 50) for _ in range(n)]
print(f'Исходный массив: {start_list}')
print(f'Отсортированнный массив: {sl(start_list)}')

print(f"Время выполнения сортировки: {timeit.timeit('sl(start_list)', setup='from __main__ import sl, start_list', number=1)}")

