"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
from random import random


def merge_two_lists(lst_1: list, lst_2: list) -> list:
    """
    Функция принимает два отсортированных по неубыванию списка чисел,
    объединяет их в один, также отсортированный по неубыванию и возвращает
    получившийся список
    """
    result_lst = []
    i = j = 0
    while i < len(lst_1) and j < len(lst_2):
        if lst_1[i] < lst_2[j]:
            result_lst.append(lst_1[i])
            i += 1
        else:
            result_lst.append(lst_2[j])
            j += 1
    if i < len(lst_1):
        result_lst += lst_1[i:]
    if j < len(lst_2):
        result_lst += lst_2[j:]
    return result_lst


def merge_sort(lst: list) -> list:
    """
    Функция принимает в качестве аргумента список чисел, сортирует его
    методом слияния списков и возвращает отсортированный список
    """
    if len(lst) == 1:
        return lst
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge_two_lists(left, right)


start_list = [random() for _ in range(10)]
result_list = merge_sort(start_list)

print('Start list:\n', start_list)
print('Result list:\n', result_list)
