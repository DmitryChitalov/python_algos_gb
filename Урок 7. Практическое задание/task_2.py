"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import random


def merge_sort(i_list):
    if len(i_list) < 2:
        return i_list

    middle = len(i_list)//2
    left_list = merge_sort(i_list[:middle])
    right_list = merge_sort(i_list[middle:])
    # print("left_list", left_list)
    # print("right_list", right_list)

    #  сюда попадем тогда, когда все ветки пройдены. Начинаем собирать листочки
    return merge(left_list, right_list)


def merge(lft_list, rght_list):
    sorted_list = []
    left_idx = right_idx = 0
    len_left, len_right = len(lft_list), len(rght_list)

    for _ in range(len_left + len_right):
        if left_idx < len_left and right_idx < len_right:
            if lft_list[left_idx] <= rght_list[right_idx]:
                sorted_list.append(lft_list[left_idx])
                left_idx += 1
            else:
                sorted_list.append(rght_list[right_idx])
                right_idx += 1

        elif left_idx == len_left:
            sorted_list.append(rght_list[right_idx])
            right_idx += 1

        elif right_idx == len_right:
            sorted_list.append(lft_list[left_idx])
            left_idx += 1

    return sorted_list


try:
    number = int(input("Массив какого размера желаете сортировать? "))
except ValueError:
    print("Некорректный ввод")
    exit()

my_list = [random()*50 for _ in range(number)]
print(my_list)
# my_list = [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
print(merge_sort(my_list))
