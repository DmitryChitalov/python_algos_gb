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
import timeit
from random import randint


def gnome_sort(sort_list):
    """
    Сортировка списка методом gnome_sort
    """
    i = 1
    while i < len(sort_list):
        if not i or sort_list[i - 1] <= sort_list[i]:
            i += 1
        else:
            sort_list[i], sort_list[i - 1] = sort_list[i - 1], sort_list[i]
            i -= 1
    return sort_list


print('Program "Find median in list"')
m = int(input('Please enter m: '))
test_lst = [randint(0, 100) for i in range(2 * m + 1)]
print(f'Test list: {test_lst}')
print(f'Sorted list(gnome sort): {gnome_sort(test_lst)}')
print(f'Median with gnome sort: {gnome_sort(test_lst)[m]}')

print(timeit.timeit("gnome_sort(test_lst[:])", setup="from __main__ import test_lst, gnome_sort", number=100))
print(timeit.timeit("gnome_sort(test_lst[:])", setup="from __main__ import test_lst, gnome_sort", number=1000))
print(timeit.timeit("gnome_sort(test_lst[:])", setup="from __main__ import test_lst, gnome_sort", number=10000))
print(timeit.timeit("gnome_sort(test_lst[:])", setup="from __main__ import test_lst, gnome_sort", number=100000))

'''
m: 10
0.0005046000000001882 - 100 
0.005011899999999958  - 1000
0.04832579999999975   - 10000
0.6988540000000003    - 100000

m: 100
0.004502299999999959  - 100 
0.051944300000000165  - 1000 
0.5975776000000002    - 10000 
6.372150300000001     - 100000

m: 1000
0.09348950000000045  - 100
0.9363090999999999   - 1000
8.9051924            - 10000
87.38602470000001    - 100000
'''