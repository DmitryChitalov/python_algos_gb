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

def merge_sort(oList, start, end):
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(oList, start, mid)
        merge_sort(oList, mid, end)
        merge_list(oList, start, mid, end)
    return oList

def merge_list(oList, start, mid, end):
    left = oList[start:mid]
    right = oList[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            oList[k] = left[i]
            i = i + 1
        else:
            oList[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            oList[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            oList[k] = right[j]
            j = j + 1
            k = k + 1

def gogo():
    original_lst = [random.random() + random.randint(0, 100) for _ in range(int(input('Кол-во эл-ов: ')))]
    print(f'Отсортированный - {merge_sort(original_lst[:], 0, len(original_lst))}')
    print(f'исходный - {original_lst}')

gogo()
