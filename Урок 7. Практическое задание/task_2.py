"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""


import numpy
from functools import reduce

user_list = numpy.random.uniform(0.0, 50.0, size=(1, int(input('Enter the number of elements: '))))
the_list = reduce(lambda x,y: x+y, user_list)
print(f'Original array is {the_list}')

    # Нашел еще одну интересную реализацию метода слияния на хабре - сделал через нее:

def merge(left_lst, right_lst):
    lst_sorted = []
    left_lst_indx = right_lst_indx = 0

    left_lst_lngth, right_lst_lngth = len(left_lst), len(right_lst)

    for _ in range(left_lst_lngth + right_lst_lngth):
        if left_lst_indx < left_lst_lngth and right_lst_indx < right_lst_lngth:
            if left_lst[left_lst_indx] <= right_lst[right_lst_indx]:
                lst_sorted.append(left_lst[left_lst_indx])
                left_lst_indx +=1
            else:
                lst_sorted.append(right_lst[right_lst_indx])
                right_lst_indx +=1
        elif left_lst_indx == left_lst_lngth:
            lst_sorted.append(right_lst[right_lst_indx])
            right_lst_indx +=1
        elif right_lst_indx == right_lst_lngth:
            lst_sorted.append(left_lst[left_lst_indx])
            left_lst_indx +=1

    return lst_sorted

def sorting(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left_lst = sorting(lst[:mid])
        right_lst = sorting(lst[mid:])
    return merge(left_lst, right_lst)

print(f'Sorted array is {sorting(the_list)}')







