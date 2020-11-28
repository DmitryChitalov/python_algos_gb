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
from statistics import median
from timeit import default_timer
from functools import wraps


class SearchMid:
    def __init__(self):
        self.m = int(input('Введите m: '))
        self.arr_src = [random.randint(-100, 100) for _ in range(2 * self.m + 1)]
        self.arr_sort = []
        self.l = len(self.arr_src)

    def _measurer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            t1 = default_timer()
            func(*args, **kwargs)
            t2 = default_timer()
            return print(f'Выполнение заняло: {(t2 - t1):.05} сек')
        return wrapper

    @_measurer
    def gnome_sort(self):
        self.arr_sort = self.arr_src[:]
        i, size = 1, len(self.arr_sort)
        while i < size:
            if self.arr_sort[i - 1] <= self.arr_sort[i]:
                i += 1
            else:
                self.arr_sort[i - 1], self.arr_sort[i] = self.arr_sort[i], self.arr_sort[i - 1]
                if i > 1:
                    i -= 1
        return print(f'\nМедиана + Гномья = {self.arr_sort[self.m]}')

    @_measurer
    def some_solution(self):
        left = []
        right = []
        interim_arr = self.arr_src
        for i in range(self.l):
            for j in range(self.l):
                if interim_arr[i] > interim_arr[j]:
                    left.append(interim_arr[j])
                if interim_arr[i] < interim_arr[j]:
                    right.append(interim_arr[j])
                if interim_arr[i] == interim_arr[j] and i > j:
                    left.append(interim_arr[j])
                if interim_arr[i] == interim_arr[j] and i < j:
                    right.append(interim_arr[j])
            if len(left) == len(right):
                mid = interim_arr[i]
                return print(f'\nМедиана без сортировки = {mid}')
            left.clear()
            right.clear()

    @_measurer
    def stat_solution(self):
        return print(f'\nМедиана + библиотека "statistics" = {median(self.arr_src)}')


item = SearchMid()
item.gnome_sort()
item.some_solution()
item.stat_solution()

"""
ЗАМЕРЫ:

m = 5000

Медиана + Гномья = 1
Выполнение заняло: 26.269 сек

Медиана без сортировки = 1
Выполнение заняло: 11.58 сек

Медиана + библиотека "statistics" = 1
Выполнение заняло: 0.0013126 сек


ВЫВОД: В очередной раз мы видим, что встроенная функция отработала гораздо быстрее, что еще раз доказывает - 
зачастую сведение решения к решению через встроенные библиотеки будет более эффективыным. 
При m = 5000, как мы видим Гномья сортировка оказалась очень медленной, это связано с тем что Гномья имеет 
среднюю сложность O(n**2), а в лучшем случае O(n). Решение без сортировки худшую сложность O(n**2), а лучшая 
может достигать O(1), когда у нас с первого раза левая и правая части будут равны.
"""