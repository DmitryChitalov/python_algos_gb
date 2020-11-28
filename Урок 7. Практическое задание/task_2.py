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


def merge_sort(unsorted):
    if len(unsorted) > 1:
        midle = len(unsorted) // 2
        left_half = unsorted[:midle]
        right_half = unsorted[midle:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                unsorted[k] = left_half[i]
                i = i + 1
            else:
                unsorted[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            unsorted[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            unsorted[k] = right_half[j]
            j = j + 1
            k = k + 1


len_list = int(input('Введите длину массива: '))
unsorted_list = [random.random() * 50 for i in range(len_list)]
print(unsorted_list)
merge_sort(unsorted_list)
print(unsorted_list)
