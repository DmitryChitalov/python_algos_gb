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
from timeit import timeit

unsorted_list = [random.uniform(0, 50) for _ in range(int(input('Введите число элементов: ')))]


def merge_sorting(input_list):
    if len(input_list) > 1:
        mid = len(input_list) // 2
        left = input_list[:mid]
        right = input_list[mid:]

        merge_sorting(left)
        merge_sorting(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                input_list[k] = left[i]
                i += 1
            else:
                input_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            input_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            input_list[k] = right[j]
            j += 1
            k += 1
        return input_list


print(f'Исходный список: {unsorted_list}')
print(f'Отсортированный список: {merge_sorting(unsorted_list)}')
print('Время выполнения:', (timeit("merge_sorting(unsorted_list[:])", globals=globals(), number=1000)))

"""
n - число элементов массива
n = 10
Время выполнения: 0.0273791000000001

n = 100
Время выполнения: 0.4137143999999999

n = 1000
Время выполнения: 5.9377555
Хороший, достаточно быстрый алгоритм.
"""
