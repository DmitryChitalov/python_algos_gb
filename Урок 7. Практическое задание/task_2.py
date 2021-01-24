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
from collections import deque


def merge_sort(raw):
    if len(raw) <= 1:
        return raw
    else:
        half = len(raw) // 2
        left = merge_sort(raw[:half])
        right = merge_sort(raw[half:])
    return merge(left, right)


def merge(left, right):
    result = []
    if left and right is not None:
        left = deque(left)
        right = deque(right)
        while left and right:
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())
    if left is not None:
        left = deque(left)
        while left:
            result.append(left.popleft())
    if right is not None:
        right = deque(right)
        while right:
            result.append(right.popleft())
    return result


n = int(input("Введите число элементов: "))
orig_list = [random.uniform(0, 50) for _ in range(n)]

print(f"Исходный массив: {orig_list}")
print(f"Отсортированный массив: {merge_sort(orig_list[:])}")

# замеры  - 10
orig_list = [random.uniform(0, 50) for _ in range(10)]
print(timeit.timeit("merge_sort(orig_list)",
                    setup="from __main__ import merge_sort, orig_list", number=1000))

# замеры - 100
orig_list = [random.uniform(0, 50) for _ in range(100)]
print(timeit.timeit("merge_sort(orig_list)",
                    setup="from __main__ import merge_sort, orig_list", number=1000))

# замеры - 1000
orig_list = [random.uniform(0, 50) for _ in range(1000)]
print(timeit.timeit("merge_sort(orig_list)",
                    setup="from __main__ import merge_sort, orig_list", number=1000))


"""
Введите число элементов: 5
Исходный массив: [49.81412226250998, 32.15722233583882, 12.67496110775841, 9.093481996539765, 18.88746543506]
Отсортированный массив: [9.093481996539765, 12.67496110775841, 18.88746543506, 32.15722233583882, 49.81412226250998]

10 значений:
    0.013762900000000133
    
100 значений:
    0.21647949999999994
    
1000 значений:
    2.6948513999999997


Вывод: С увелечеием размера последовательности растет время её сортировки.
"""