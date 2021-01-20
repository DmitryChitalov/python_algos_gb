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


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

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


if __name__ == "__main__":
    test_list = [random.triangular(0, 50) for elem in range(100)]
    test_list_int = [random.randint(0, 50) for _ in range(100)]
    print(f'исходный массив: {test_list}')
    print(f'Отсортированный массив: {merge_sort(test_list[:])}')
    print('Профилировка времени сортировки слиянием')
    print(timeit(
        "merge_sort(test_list[:])",
        setup="from __main__ import merge_sort, test_list", number=1000)
    )
    print(timeit(
        "merge_sort(test_list_int[:])",
        setup="from __main__ import merge_sort, test_list_int", number=1000)
    )

"""
Выводы: Сортировка слиянием работает в несколько раз эффективнее, чем сотрировка пузырьком.
Время, затраченное на сортировку массива, почти в 4 раза меньше.
"""

