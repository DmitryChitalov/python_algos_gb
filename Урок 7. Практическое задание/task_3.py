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
from collections import deque
from timeit import timeit


def median_cust_1(m, arr):
    result = deque(arr)
    while len(result) > m:
        med = max(result)
        result.remove(med)
    return med


def median_cust_2(arr, k=0):
    if len(arr) == 1:
        return arr[0]
    if isinstance(arr, list):
        arr = deque(arr)
        k = len(arr) / 2
    piv = choice(arr)
    left, right, same = deque(), deque(), deque()
    while arr:
        el = arr.pop()
        if el < piv:
            left.append(el)
        if el > piv:
            right.append(el)
        if el == piv:
            same.append(el)
    if k < len(left):
        return median_cust_2(left, k)
    elif k < len(left) + len(same):
        return same[0]
    else:
        return median_cust_2(right, k - len(left) - len(same))


m = int(input('Введите m: '))
arr = [randint(-10, 10) for _ in range(2 * m + 1)]

print(f'Standart median : {median(arr)}')
print(f'Custom median first : {median_cust_1(m, arr)}')
print(timeit("median_cust_1(m, arr)", "from __main__ import median_cust_1, arr, m", number=100))
print(f'Custom median second : {median_cust_2(arr)}')
print(timeit("median_cust_2(arr)", "from __main__ import median_cust_2, arr", number=100))
