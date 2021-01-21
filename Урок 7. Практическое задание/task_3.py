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
import random
from functools import total_ordering
from bisect import bisect_left
from heapq import merge
from statistics import median
from timeit import timeit


# Нахождение медианы с помощью алгоритма quick_select
def quick_select_median(arr, pivot_fn=random.choice):
    if len(arr) % 2 == 1:
        return quick_select(arr, len(arr) / 2, pivot_fn)
    else:
        return 0.5 * (quick_select(arr, len(arr) / 2 - 1, pivot_fn) + quick_select(arr, len(arr) / 2, pivot_fn))


def quick_select(arr, k, pivot_fn):
    if len(arr) == 1:
        return arr[0]

    pivot = pivot_fn(arr)

    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quick_select(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quick_select(highs, k - len(lows) - len(pivots), pivot_fn)


# Пасьянсная сортировка
@total_ordering
class Pile(list):
    def __lt__(self, other): return self[-1] < other[-1]
    def __eq__(self, other): return self[-1] == other[-1]


def patience_sort(arr):
    piles = []
    for x in arr:
        new_pile = Pile([x])
        i = bisect_left(piles, new_pile)
        if i != len(piles):
            piles[i].append(x)
        else:
            piles.append(new_pile)

    arr[:] = merge(*[reversed(pile) for pile in piles])
    return arr


# Нахождение медианы с через пасьянсную сортировку
def patience_sort_median(arr):
    arr = patience_sort(arr)
    if len(arr) % 2 == 1:
        return arr[len(arr) // 2]
    else:
        return 0.5 * (arr[len(arr) // 2 - 1] + arr[len(arr) // 2])


if __name__ == '__main__':
    m = int(input('Введите натуральное число: '))
    a = [random.randint(1, 1000) for _ in range(2 * m + 1)]
    print('Нахождение медианы через функцию median: ', median(a.copy()))
    print('Нахождение медианы через функцию quick_select_median: ', quick_select_median(a.copy()))
    print('Нахождение медианы через функцию patience_sort_median: ', patience_sort_median(a.copy()))
    print(timeit('quick_select_median(b)', 'b = a.copy()', number=1, globals=globals()))
    print(timeit('patience_sort_median(b)', 'b = a.copy()', number=1, globals=globals()))
    print(timeit('median(b)', 'b = a.copy()', number=1, globals=globals()))
