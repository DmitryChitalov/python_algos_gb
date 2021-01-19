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
from statistics import median
from random import randint
from task_2 import my_sort
from timeit import timeit


def get_m_row(m):
    return [randint(-100, 100) for i in range(2 * m + 1)]


def get_me_median(arr):
    i = 0
    while i < len(arr) - 1:
        r, l, delta = 0, 0, 1 # ага, мораль - обнуляйте переменнные
        test_arr = arr[:]
        candidate = test_arr.pop(i)
        for j in test_arr:
            if j > candidate:
                r += 1
            elif j < candidate:
                l += 1
            else:
                delta += 1
        if abs(r-l) <= delta:
            return candidate
        i += 1


if __name__ == '__main__':
    m = 10
    arr = get_m_row(m)
    # arr = [-23, -91, 43, -51, -68, 13, -42, -31, -28, -49, 42, 61, -23, -41, 87, 39, 92, 60, 10, 26, -60]
    print(arr)
    print(median(arr))
    print(get_me_median(arr))  # вроде без сортировки и работает.
    print(my_sort(arr)[m]) # ну просто посмотреть
    print(timeit('median(arr)', setup= 'from __main__ import median, arr', number=1000))
    print(timeit('get_me_median(arr)', setup= 'from __main__ import get_me_median, arr', number=1000))
    print(timeit('my_sort(arr[:])[m]', setup='from __main__ import my_sort, m, arr', number=1000))
    """
    0.0007125999999999938
    0.023562100000000002
    0.0336813
    Мой метод  работает медленнее штатного определения медианы из statistics, 
    но быстрее взятия середины ряда даже с относительно быстрой сортировкой слиянием.
    """

