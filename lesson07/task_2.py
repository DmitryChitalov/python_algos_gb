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
from timeit import timeit
from random import random


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


def my_merge_sort(lst_arg):
    if len(lst_arg) > 1:
        center = len(lst_arg) // 2
        left = lst_arg[:center]
        right = lst_arg[center:]
        my_merge_sort(left)
        my_merge_sort(right)

        return sorted(left + right)


number = int(input("Введите число элементов: "))
my_list = [50 * random() for el in range(number)]
print(f"Исходный - {my_list}")
print(f"Отсортированный - {my_merge_sort(my_list[:])}")

# замеры

for num in (10, 100, 1000):
    my_list = [50 * random() for el in range(num)]
    print(f"merge_sort num= {num}: ",
          timeit(f"merge_sort(my_list[:])", globals=globals(), number=1000))
    print(f"my_merge_sort num= {num}: ",
          timeit(f"my_merge_sort(my_list[:])", globals=globals(), number=1000))

'''
Для замеров сравнивал две функции - первая с урока, вторая для слияния
использует стандартную быструю сортировку. Замеры показывают, что использование
стандартной сортировки для слияния двух списков значительно ускоряют сортировку
слиянием:)

merge_sort num= 10:  0.018746300000000105
my_merge_sort num= 10:  0.011775000000000091
merge_sort num= 100:  0.2712502999999997
my_merge_sort num= 100:  0.10411020000000004
merge_sort num= 1000:  3.9571501
my_merge_sort num= 1000:  1.5301520000000002
'''