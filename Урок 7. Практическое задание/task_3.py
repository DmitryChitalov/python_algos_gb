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


def is_median(in_ind, in_arr):
    left = 0
    right = 0
    print(f'Check {in_arr[in_ind]}')
    for i in range(len(in_arr)):
        if in_arr[i] < in_arr[in_ind]:
            left += 1
        else:
            if in_arr[i] > in_arr[in_ind]:
                right += 1
    if left == right: return True
    if len(in_arr) % 2 == 0 and abs(left - right) == 1: return True
    return False


def get_median(in_arr):
    median1 = None
    median2 = None
    for i in range(len(in_arr)):
        if is_median(i, in_arr):
            if median1 is None:
                median1 = in_arr[i]
            else:
                median2 = in_arr[i]
    if median2 is None: median2 = median1
    return (median1 + median2) / 2


num_arr = [random.randint(0, 20) for _ in range(7)]
print(num_arr)
print(get_median(num_arr))
