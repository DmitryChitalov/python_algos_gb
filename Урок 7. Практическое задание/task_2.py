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

n = int(input('Введите количество элементов: '))
my_list = [(uniform(0, 50)) for i in range(n)]

def merge_algoritm(some_list):
    if len(some_list) <= 1:
        return some_list
    else:
        center = len(some_list) // 2
        left = some_list[:center]
        right = some_list[center:]

        merge_algoritm(left)
        merge_algoritm(right)

        i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            some_list[k] = left[i]
            i += 1
        else:
            some_list[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        some_list[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        some_list[k] = right[j]
        j += 1
        k += 1
    return some_list

print(f'Исходный список - {my_list}\nОтсортированный список - {merge_algoritm(my_list)}')