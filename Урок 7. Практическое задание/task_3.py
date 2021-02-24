"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]

left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()
"""
"""
Для массива с нечетным количеством элементов медиана является элементом массива. 
Для массива с нечетным - среднее двух ближайших к медиане значений
"""

from timeit import timeit
import random
from statistics import median


def is_median(in_ind, in_arr, in_flag):
    left = 0
    right = 0
    for i in range(len(in_arr)):
        if in_arr[i] < in_arr[in_ind]:
            left += 1
        else:
            if in_arr[i] > in_arr[in_ind]:
                right += 1
    if left == right: return True
    if (len(in_arr) % 2 == 0 or in_flag ) and abs(left - right) == 1: return True
    return False


def get_median(in_arr):
    median = None
    for i in range(len(in_arr)):
        if is_median(i, in_arr, False):
            median = in_arr[i]
    if median is None:
        for i in range(len(in_arr)):
            if is_median(i, in_arr, True ):
                median = in_arr[i]
    return median


print('Input number:')
qty = int(input()) * 2 + 1
print(f'Array of 2 * n + 1 = {qty} elements')
num_arr = [random.randint(0, 20) for _ in range(qty)]
print(num_arr)
print(f'Median is {get_median(num_arr)}')
