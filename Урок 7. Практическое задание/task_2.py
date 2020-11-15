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


def merge_sort(lst):
    if len(lst) > 1:
        lst_left = lst[:len(lst) // 2]
        lst_right = lst[len(lst) // 2:]
        lst.clear()
        merge_sort(lst_left)
        merge_sort(lst_right)

        while lst_left or lst_right:
            if not lst_left:
                lst.extend(lst_right)
                break
            if not lst_right:
                lst.extend(lst_left)
                break

            if lst_left[0] < lst_right[0]:
                lst.append(lst_left.pop(0))
            else:
                lst.append(lst_right.pop(0))

    return lst


n = int(input("Введите число элементов: "))
list_obj = [round(50 * random.random(), 3) for _ in range(n)]
print(f'Исходный - {list_obj}')
print(f'Отсортированный - {merge_sort(list_obj)}')
