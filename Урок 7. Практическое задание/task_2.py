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
from time import time
import memory_profiler


def sort_1(lst):
    if len(lst) > 1:
        center = len(lst) // 2
        left, right = lst[:center], lst[center:]

        sort_1(left)
        sort_1(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

        return lst


def custom_profiler(f):
    def decorate(lst):
        repeat_count = 1000
        m1 = memory_profiler.memory_usage()
        t1 = time()

        for _ in range(repeat_count):
            f(lst[:])

        t2 = time()
        m2 = memory_profiler.memory_usage()
        print(f"Среднееи время выполнения: {(t2 - t1) / repeat_count}")
        print(f"Использование памяти всего за {repeat_count} прогонов: {m2[0] - m1[0]}")
        return
    return decorate


@custom_profiler
def sort_profile(lst):
    return sort_1(lst)


# Генерация списка
source_list = [(random() * 50) for _ in range(10)]
# Вывод исходного списка
print(source_list)

# Сортировка списка
sorted_list_1 = sort_1(source_list[:])
print(sorted_list_1)

# Профилирование сортировки
source_list_2 = [(random() * 50) for _ in range(1000)]
sorted_list_2 = sort_profile(source_list_2[:])
