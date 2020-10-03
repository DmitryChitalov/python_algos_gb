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
сделал два решения:
1 - своя функция
2 - гномья сортировка

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1000    0.001    0.000    0.003    0.000 statistics.py:414(median)
     1000    0.010    0.000    0.022    0.000 task_3.py:35(get_median)
     1000    0.001    0.000    1.830    0.002 task_3.py:59(stooge)
     
Вывод:
Самая быстая median from statistics,
Вторая по скорости это моя функция,
гномья сортировка очень медленная
"""

import cProfile
import random
from statistics import median


def create_list(m: int) -> list:
    return [random.randint(0, 50) for x in range(2 * m + 1)]


def get_median(my_list_in: list) -> int:
    left_list = []
    i = len(my_list_in) // 2
    for _ in range(i + 1):
        tmp = min(my_list_in)
        left_list.append(tmp)
        my_list_in.pop(my_list_in.index(tmp))
    tmp_list = left_list + my_list_in
    return tmp_list[i]


def stooge_rec_a(data, i=0, j=None):
    if j is None:
        j = len(data) - 1
    if data[j] < data[i]:
        data[i], data[j] = data[j], data[i]
    if j - i > 1:
        t = (j - i + 1) // 3
        stooge_rec_a(data, i, j - t)
        stooge_rec_a(data, i + t, j)
        stooge_rec_a(data, i, j - t)
    return data


def stooge(data):
    return stooge_rec_a(data, 0, len(data) - 1)


def main():
    for _ in range(1000):
        x = 100
        my_list = create_list(x)
        print(median(my_list))
        print(get_median(my_list.copy()))
        print(stooge(my_list.copy())[x])


# main()
cProfile.run('main()')
