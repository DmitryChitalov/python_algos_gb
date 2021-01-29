"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""


import numpy as np
import operator
import timeit


def merge_sort(L, compare=operator.lt):
    def merge(left, right, compare):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if compare(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


orig_list = [np.random.uniform(0, 50) for _ in range(int(input("Введите число элементов: ")))]


print(f"Исходный массив: {orig_list}")
sorted_array = merge_sort(orig_list[:])
print(f"Отсортированный массив: {sorted_array}")


# замеры 10
print(timeit.timeit("merge_sort(orig_list)",
    setup="from __main__ import merge_sort, orig_list", number=1000))


# замеры 100
orig_list = [np.random.uniform(0, 50) for _ in range(100)]
print(timeit.timeit("merge_sort(orig_list)",
    setup="from __main__ import merge_sort, orig_list", number=1000))


# замеры 1000
orig_list = [np.random.uniform(0, 50) for _ in range(1000)]
print(timeit.timeit("merge_sort(orig_list)",
    setup="from __main__ import merge_sort, orig_list", number=1000))


"""
Введите число элементов: 5
Исходный массив: [28.287066169022886, 19.751334426204586, 8.632535143043963, 1.4044226398419346, 20.98763623619232]
Отсортированный массив: [1.4044226398419346, 8.632535143043963, 19.751334426204586, 20.98763623619232, 28.287066169022886]
0.005014600000000202
0.1991335999999999
2.8288609000000005
Видно, что с ростом массива время растет, но не в квадратичной последовательности, а как и надо O(NlogN)
"""
