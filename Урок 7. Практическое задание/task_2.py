"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from timeit import timeit
from random import random
import operator


def print_timeint(func_name, n):
    print(f'{func_name} {timeit(f"{func_name}({n})", globals=globals(), number=10000)}')


def my_merge_sort(lst_arg):
    if len(lst_arg) > 1:
        center = len(lst_arg) // 2
        left = lst_arg[:center]
        right = lst_arg[center:]
        my_merge_sort(left)
        my_merge_sort(right)

        return sorted(left + right)



def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


number = int(input("Введите число элементов: "))
my_list = [50 * random() for el in range(number)]
print(f"Исходный - {my_list}")
print(f"Отсортированный - {merge_sort(my_list)}")
print(f"Отсортированный - {my_merge_sort(my_list)}")

print_timeint('merge_sort', my_list)
print_timeint('my_merge_sort', my_list)

"""
Введите число элементов: 5
Исходный - [5.9596067276123765, 44.468521600737134, 2.480465338649551, 11.063196106111295, 30.68096737164394]
Отсортированный - [2.480465338649551, 5.9596067276123765, 11.063196106111295, 30.68096737164394, 44.468521600737134]
Отсортированный - [2.480465338649551, 5.9596067276123765, 11.063196106111295, 30.68096737164394, 44.468521600737134]
merge_sort 0.04672119999999991
my_merge_sort 0.02621870000000026

стандартная сортирвка работает лучше
"""