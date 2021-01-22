"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import timeit
from random import random
from task_1 import bubble_sort2


def merge_sort(lst):
    if len(lst) > 1:
        center = len(lst) // 2
        left = lst[:center]
        right = lst[center:]
        merge_sort(left)
        merge_sort(right)

        left_index, right_index, sorted_index = 0, 0, 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                lst[sorted_index] = left[left_index]
                left_index += 1
            else:
                lst[sorted_index] = right[right_index]
                right_index += 1
            sorted_index += 1

        while left_index < len(left):
            lst[sorted_index] = left[left_index]
            left_index += 1
            sorted_index += 1

        while right_index < len(right):
            lst[sorted_index] = right[right_index]
            right_index += 1
            sorted_index += 1
        return lst


while True:
    try:
        n = int(input('Введите количество элементов: '))
    except ValueError:
        print('Ошибка ввода!')
    else:
        num_lst = [random() * 50 for _ in range(n)]
        print(f'Исходный массив:\n{num_lst}')
        print(f'Отсортированный массив:\n{merge_sort(num_lst)}')
        break


lst1 = [random() * 50 for _ in range(100)]
lst2 = [random() * 50 for _ in range(1000)]
lst3 = [random() * 50 for _ in range(10000)]
print('Замеры: ')
print(timeit.timeit("merge_sort(lst1)", setup="from __main__ import merge_sort, lst1", number=100))
print(timeit.timeit("merge_sort(lst2)", setup="from __main__ import merge_sort, lst2", number=100))
print(timeit.timeit("merge_sort(lst3)", setup="from __main__ import merge_sort, lst3", number=100))

lst4 = [random() * 50 for _ in range(10000)]
print(timeit.timeit("lst4.sort()", setup="from __main__ import lst4", number=100))

lst5 = [random() * 50 for _ in range(10000)]
print(timeit.timeit("bubble_sort2(lst5)", setup="from __main__ import bubble_sort2, lst5", number=100))

'''
Замеры: 
0.03250410000000015
0.23397253299999976
2.879734428
0.003869204000000792
7.453742723
'''
# Как видно по замерам, сортировка слиянием гораздо быстрее пузырька,
# однако обе функции проигрывают встроенному методу sort() для списка