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
from random import randint, choice
from statistics import median


def my_median(lst):
    if len(lst) % 2 == 1:
        return select(lst, len(lst) / 2)
    else:
        return 0.5 * (select(lst, len(lst) / 2 - 1) + select(lst, len(lst) / 2))


def select(l, k):
    if len(l) == 1:
        return l[0]

    pivot = choice(l)

    left = [el for el in l if el < pivot]
    right = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(left):
        return select(left, k)
    elif k < len(left) + len(pivots):
        return pivots[0]
    else:
        return select(right, k - len(left) - len(pivots))


if __name__ == '__main__':
    m = 5
    lst = [randint(0, 100) for _ in range(2 * m + 1)]
    print(lst)
    print(median(lst))
    median_num = my_median(lst)
    print(median_num)
