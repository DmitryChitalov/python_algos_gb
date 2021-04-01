"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import uniform
from timeit import timeit


def merge_sort(lst):

    n = len(lst)

    if n < 2:
        return lst

    left = merge_sort(lst[:n//2])
    right = merge_sort(lst[n//2:n])

    i = j = 0

    result = []

    while i < len(left) or j < len(right):

        if not i < len(left):
            result.append(right[j])
            j += 1
        elif not j < len(right):
            result.append(left[i])
            i += 1
        elif right[j] > left[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result


number = int(input('\nВведите число элементов: '))
nums_array = [uniform(0.00, 49.99) for _ in range(number)]
print('Исходный массив:', nums_array)
nums_array = merge_sort(nums_array)
print('Отсортированный массив:', nums_array, '\n')


# Замеры на массивах разной длины:

test_nums = (10, 100, 1000)

test_arrays = tuple([uniform(0.00, 49.99) for _ in range(num)] for num in test_nums)

for array in test_arrays:
    print(f'Массив на {len(array)} элементов: {timeit("merge_sort(array[:])", globals=globals(), number=1000)}')

# Массив на 10 элементов: 0.009952000000000183
# Массив на 100 элементов: 0.15717959999999964
# Массив на 1000 элементов: 2.2101195000000002
