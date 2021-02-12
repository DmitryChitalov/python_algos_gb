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


def merge_sort(i_lst):
    if len(i_lst) <= 1:
        return i_lst
    l_mid = len(i_lst) // 2
    l_left, l_right = merge_sort(i_lst[:l_mid]), merge_sort(i_lst[l_mid:])

    l_left_cursor, l_right_cursor = 0, 0
    while l_left_cursor < len(l_left) and l_right_cursor < len(l_right):

        if l_left[l_left_cursor] <= l_right[l_right_cursor]:
            i_lst[l_left_cursor + l_right_cursor] = l_left[l_left_cursor]
            l_left_cursor += 1
        else:
            i_lst[l_left_cursor + l_right_cursor] = l_right[l_right_cursor]
            l_right_cursor += 1

    for l_left_cursor in range(l_left_cursor, len(l_left)):
        i_lst[l_left_cursor + l_right_cursor] = l_left[l_left_cursor]

    for l_right_cursor in range(l_right_cursor, len(l_right)):
        i_lst[l_left_cursor + l_right_cursor] = l_right[l_right_cursor]

    return i_lst


g_cnt = int(input('Введите число элементов: '))
g_lst = [uniform(0, 50) for i in range(g_cnt)]
print('Исходный -', g_lst)
print(timeit("merge_sort(g_lst[:])", globals=globals(), number=10))
print(timeit("merge_sort(g_lst[:])", globals=globals(), number=100))
print(timeit("merge_sort(g_lst[:])", globals=globals(), number=1000))
print(timeit("merge_sort(g_lst[:])", globals=globals(), number=10000))
print(timeit("merge_sort(g_lst[:])", globals=globals(), number=100000))
merge_sort(g_lst)
print('Отсортированный -', g_lst)
#
# Данный алгоритм очень эффективный, что показывает статистика ниже
# для 100 элементов.
# 0.00178300000000009
# 0.02015520000000004
# 0.18874919999999973
# 1.8128367
# 18.8269083
