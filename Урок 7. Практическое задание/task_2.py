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

def sorts(user_list):
    if len(user_list) > 1:
        center = len(user_list) // 2
        left = user_list[:center]
        right = user_list[center:]
        sorts(left)
        sorts(right)
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                user_list[k] = left[i]
                i += 1
            else:
                user_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            user_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            user_list[k] = right[j]
            j += 1
            k += 1
        return user_list





user_number = int(input("Введите количество чисел массива: "))
my_list = [random.random() * 50 for i in range(user_number)]
print(f'Исходный массив: {my_list}')
print(f'Отсортированный массив: {sorts(my_list)}')