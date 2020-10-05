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

nums = int(input('Введите число элементов: '))


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


orig_list = [uniform(0, 50) for _ in range(nums)]
print(f'Исходный массив: {orig_list}')
print(f'Отсортированный массив: {merge_sort(orig_list)}')

print(timeit("merge_sort(orig_list)", \
             setup="from __main__ import merge_sort, orig_list", number=1))

'''nums = 10
затрачено времени: 6.784501601941884e-05

nums = 100
затрачено времени: 0.0007321459997911006

nums = 100000
затрачено времени: 0.3261981389950961

nums = 1 000 000
затрачено времени: 4.780807729985099

Вывод: сортировка слиянием значительно быстрее сортировки пузырьком
'''
