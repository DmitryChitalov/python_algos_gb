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


def count_input():
    try:
        return int(input('Введите число элементов:'))
    except:
        print('Вы ввели не целое число')
        return count_input()


def merge_sort(sorting_array):
    def __inner_sorting_func(copy_array):
        __length = len(copy_array)
        if __length > 2:
            __left = __inner_sorting_func(copy_array[:__length // 2])
            __right = __inner_sorting_func(copy_array[__length // 2:])
            copy_array = __left + __right
            last_index = len(copy_array) - 1

            for i in range(last_index):
                min_value = copy_array[i]
                min_index = i

                for j in range(i + 1, last_index + 1):
                    if min_value > copy_array[j]:
                        min_value = copy_array[j]
                        min_index = j

                if min_index != i:
                    copy_array[i], copy_array[min_index] = copy_array[min_index], copy_array[i]

        elif len(copy_array) > 1 and copy_array[0] > copy_array[1]:
            copy_array[0], copy_array[1] = copy_array[1], copy_array[0]

        return copy_array

    __sorted_array = sorting_array.copy()
    return __inner_sorting_func(__sorted_array)


initial_array = list(random.uniform(0, 50) for _ in range(0, count_input()))
print(initial_array)
print(merge_sort(initial_array))
print(initial_array)
