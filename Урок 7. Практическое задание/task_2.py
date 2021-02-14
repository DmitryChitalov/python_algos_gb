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


def generate_array():
    """
    Генерация массива вещественных чисел
    :return: возврашает сгенерированный массив
    """
    number = int(input("Введие число элементов : "))
    return [uniform(0.0, 50.0) for element in range(1, number)]


def sort_merger(array):
    if len(array) > 1:
        center_array = len(array) // 2
        left_side = array[:center_array]
        right_side = array[center_array:]
        sort_merger(left_side)
        sort_merger(right_side)
        left_count, right_count, main_count = 0, 0, 0
        while left_count < len(left_side) and right_count < len(right_side):
            if left_side[left_count] < right_side[right_count]:
                array[main_count] = left_side[left_count]
                left_count += 1
            else:
                array[main_count] = right_side[right_count]
                right_count += 1
            main_count += 1
        while left_count < len(left_side):
            array[main_count] = left_side[left_count]
            left_count += 1
            main_count += 1
        while right_count < len(right_side):
            array[main_count] = right_side[right_count]
            right_count += 1
            main_count += 1
        return array


source_array = generate_array()
print("Исходный массив : ", source_array)
print("Отсортированный массив : ", sort_merger(source_array))
print("Время выполнения : ")
print(timeit("sort_merger(source_array)", "from __main__ import sort_merger , source_array", number=1000))

"""
Введие число элементов : 8
Исходный массив :  [46.071411682769906, 44.16414924197512, 35.77328608919797, 22.197589027955495, 35.24154395253212, 24.11510644468629, 16.814512146606432]
Отсортированный массив :  [16.814512146606432, 22.197589027955495, 24.11510644468629, 35.24154395253212, 35.77328608919797, 44.16414924197512, 46.071411682769906]
Время выполнения : 
0.02491948900023999
"""
