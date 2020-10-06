"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
from statistics import median
from random import randint


def median_func(lst):
    mdn_idx = (len(lst) - 1) // 2
    mdn = lst[mdn_idx]
    left, right = lst[:mdn_idx], lst[mdn_idx + 1:]
    max_left, min_right = max(left), min(right)
    go = True
    while go:
        if max_left > mdn:
            i = left.index(max_left)
            left[i], mdn = mdn, left[i]
            max_left = max(left)
        elif min_right < mdn:
            j = right.index(min_right)
            right[j], mdn = mdn, right[j]
            min_right = min(right)
        else:
            go = False
    return mdn


list_origin = [randint(0, 100) for _ in range(11)]

print(median_func(list_origin))
print(median(list_origin))
