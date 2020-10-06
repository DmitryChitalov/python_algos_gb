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
"""
Выполнил поиск медианы без сортировки. Сделал проверку работы функции, встроенными средствами библиотеки
statistics.
"""
import random
from statistics import median


def find_m(i):
    left = []
    right = []
    for idx, val in enumerate(array):
        if val <= array[i] and idx != i:
            left.append(val)
        elif val >= array[i] and idx != i:
            right.append(val)
    if len(left) == len(right):
        return True


m_val = 10
array = [random.randint(-100, 100) for _ in range(2 * m_val + 1)]
print(f'Random array = {array}')

for i_check, val in enumerate(array):
    if find_m(i_check):
        print(f'Without sort array: median = {array[i_check]}')

print(f'Check by statistic: median = {median(array)}')