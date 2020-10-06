"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import uniform
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


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj) - 1:
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [uniform(0, 50) for _ in range(5)]
orig_list_copy1 = orig_list.copy()
orig_list_copy2 = orig_list.copy()
print(f"Пузырек: "
      f"{timeit('bubble_sort(orig_list_copy1)', 'from __main__ import bubble_sort, orig_list_copy1', number=10000)}")
print(f"Слияние: "
      f"{timeit('merge_sort(orig_list_copy2)', 'from __main__ import merge_sort, orig_list_copy2', number=10000)}")
print(f'Оригинальный массив: {orig_list}')
print(f'Массив отсортированный пузырьком: {orig_list_copy1}')
print(f'Массив отсортированный слиянием: {orig_list_copy2}')
"""
Сравнивал сортировку слиянием с пузырьком.

Чем больше список, тем слияние эффективнее пузырька. На 100 элементах слияние быстрее примерно в 2 раза, а
на 300 элементах слияние быстрее почти в 6 раз.
На 100 элементах:           На 300 элементах:
Пузырек: 9.421386796        Пузырек: 76.109343086
Слияние: 4.134829148        Слияние: 13.692862849999997

Если же элементов в списке мало, то пузырек отрабатывает чуть-чуть быстрее.
На 5 элементах:
Пузырек: 0.039427427
Слияние: 0.095654057
"""
