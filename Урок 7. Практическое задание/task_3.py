"""
3. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...
"""
from random import randint


def shell_sort(lst):
    d = len(lst) // 2
    while d:
        for i, el in enumerate(lst):
            while i >= d and lst[i - d] > el:
                lst[i] = lst[i - d]
                i -= d
            lst[i] = el
        d = 1 if d == 2 else int(d * 5.0 / 11)
    return lst


def find_median(m: int) -> int:
    lst = [randint(-100, 100) for _ in range(2 * m + 1)]
    print('List:', lst)
    sorted_lst = shell_sort(lst[:])
    return sorted_lst[m]


print('Median is:', find_median(3))


# Without sort


def find_median_without_sort(m: int) -> int:
    lst = [randint(-100, 100) for _ in range(2 * m + 1)]
    print('List:', lst)
    tmp = lst[:]
    for i in range(m):
        tmp.remove(max(tmp))
    return max(tmp)


print('Median is:', find_median_without_sort(3))
