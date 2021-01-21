"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). ---- 1
Выведите на экран исходный ---- 2
и отсортированный массивы. ---- 3

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import random


# сортировка слиянием ---- 1
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = 0
    right_list_index = 0
    left_list_length = len(left_list)
    right_list_length = len(right_list)
    for i in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list


def merge_sort(lst_obj):
    if len(lst_obj) <= 1:
        return lst_obj

    mid = len(lst_obj) // 2

    left_lst = merge_sort(lst_obj[:mid])
    right_lst = merge_sort(lst_obj[mid:])
    return merge(left_lst, right_lst)


# формирование исходного списка и вывод исходного и отсортированного списков ---- 2 и 3
def random_list():
    try:
        n = int(input('Введите число элементов: \n'))
    except ValueError:
        return f'Вы указали неверное значение'
    if n <= 0:
        return f'Число элементов не может быть меньше либо равным нулю'
    else:
        randoms_list = [random()*50 for _ in range(n)]
    return f'Исходный список: {randoms_list}\n' \
           f'Отсортированный список: {merge_sort(randoms_list)}'


print(random_list())

"""
Результат:
7 
Исходный список: [0.9808636156510009, 12.507054904114801, 1.733227791138181, 47.93808285133672, 30.98995332192444, 12.448046633776954, 1.5729145814221857]
Отсортированный список: [0.9808636156510009, 1.5729145814221857, 1.733227791138181, 12.448046633776954, 12.507054904114801, 30.98995332192444, 47.93808285133672]
"""
