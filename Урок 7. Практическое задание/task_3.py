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
import random
from statistics import median


def med(a):
    def r_sort(a):
        if len(a) <= 1:
            return a
        else:
            q = random.choice(a)
            L = []
            M = []
            R = []
            for elem in a:
                if elem < q:
                    L.append(elem)
                elif elem > q:
                    R.append(elem)
                else:
                    M.append(elem)
            return r_sort(L) + M + r_sort(R)
    return r_sort(a)

m = int(input('Введите число элементов: '))
start_list = [random.randint(-100, 100) for _ in range(2*m + 1)]
print(start_list)

print(f'Проверка через модуль median {median(start_list)}')

x = med(start_list)
print(f'Отсортированный список {x}')
print(f'Медиана: {x[m]}')

"""Время выполнения"""
print(timeit.timeit("med(start_list)", \
    setup="from __main__ import med, start_list", number=1))