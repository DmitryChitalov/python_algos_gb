"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import random as rd
from timeit import timeit


def gen_numb():
    while True:
        new_numb = rd.random() * 50
        if new_numb != 50:
            return new_numb


def merge_sort(lst):
    def do_merge(left_part, right_part):
        result = []
        left_idx, right_idx = 0, 0
        left_length, right_length = len(left_part), len(right_part)

        for idx in range(left_length + right_length):
            if left_idx < left_length and right_idx < right_length:
                # Сравниваем первые элементы в начале каждого списка.
                if left_part[left_idx] <= right_part[right_idx]:
                    result.append(left_part[left_idx])
                    left_idx += 1
                else:
                    result.append(right_part[right_idx])
                    right_idx += 1
            elif left_idx == left_length:
                result.append(right_part[right_idx])
                right_idx += 1
            elif right_idx == right_length:
                result.append(left_part[left_idx])
                left_idx += 1

        return result


    if len(lst) > 1:
        center = len(lst) // 2
        left_list = merge_sort(lst[:center])
        right_list = merge_sort(lst[center:])

        return do_merge(left_list, right_list)
    else:
        return lst



my_list = [gen_numb() for _ in range(int(input('[?] Введите число элементов: ')))]
print(f'[1] Сгенерированный список:  {my_list}')
sort_list = merge_sort(my_list)
print(f'[2] Отсортированный список:  {sort_list}')

"""
Результат выполнения:
    [?] Введите число элементов: 5
    [1] Сгенерированный список:  [16.910911663357993, 5.164266584375571, 3.3770070605420646, 25.54880807839496, 42.745639513485415]
    [2] Отсортированный список:  [3.3770070605420646, 5.164266584375571, 16.910911663357993, 25.54880807839496, 42.745639513485415]
"""
