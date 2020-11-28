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

my_list = [uniform(0, 50) for _ in range(10)]
print(my_list)


def merge(lst):
    if len(lst) < 2:
        return lst
    avrg = len(lst) // 2
    left = merge(lst[:avrg])
    right = merge(lst[avrg:])

    return merge_sort(left, right)


def merge_sort(left_list, right_list):
    temp = []
    left_index = right_index = 0
    for _ in range(len(left_list) + len(right_list)):
        if left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] > right_list[right_index]:
                temp.append(right_list[right_index])
                right_index += 1
            else:
                temp.append(left_list[left_index])
                left_index += 1
        elif left_index == len(left_list):
            temp.append(right_list[right_index])
            right_index += 1
        elif right_index == len(right_list):
            temp.append(left_list[left_index])
            left_index += 1

    return temp


print(merge(my_list))
