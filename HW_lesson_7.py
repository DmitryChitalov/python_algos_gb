# ////////////////////////////////////////////  Task 1  ///////////////////////////////////////////////////////////////

"""1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение.
Обязательно сделайте замеры времени обеих реализаций и обосновать дала ли оптимизация эффективность.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере, а по убыванию.
"""

import timeit
import random
from statistics import median


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_mod(lst_obj):
    n = 0
    flag = True
    while flag and (n < len(lst_obj)):
        for i in range(len(lst_obj) - n - 1):
            if lst_obj[i] < lst_obj[i + 1]:  # decreasing
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = False
        if not flag:
            n += 1
            flag = True
        else:
            break
    return lst_obj


# замеры 10
print()
orig_list = [random.randint(-100, 100) for _ in range(10)]
print(f'Исходный массив из 10:\n{orig_list}')

print('\nLead time bubble_sort(): \t\t', timeit.timeit("bubble_sort(orig_list[:])", setup="from __main__ import "
                                                                                          "bubble_sort, orig_list",
                                                       number=1))
print('Lead time bubble_sort_mod(): \t', timeit.timeit("bubble_sort_mod(orig_list[:])", setup="from __main__ import "
                                                                                              "bubble_sort_mod, "
                                                                                              "orig_list", number=1))
print(f'\nОтсортированный массив:\n{bubble_sort_mod(orig_list)}')

# замеры 100
print()
orig_list = [random.randint(-100, 100) for _ in range(100)]
print(f'Исходный массив из 100:\n{orig_list}')

print('\nLead time bubble_sort(): \t\t', timeit.timeit("bubble_sort(orig_list[:])", setup="from __main__ import "
                                                                                          "bubble_sort, orig_list",
                                                       number=1))
print('Lead time bubble_sort_mod(): \t', timeit.timeit("bubble_sort_mod(orig_list[:])", setup="from __main__ import "
                                                                                              "bubble_sort_mod, "
                                                                                              "orig_list", number=1))
print(f'\nОтсортированный массив:\n{bubble_sort_mod(orig_list)}')

# замеры 1000
print()
orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(f'Исходный массив из 1000:\n{orig_list}')

print('\nLead time bubble_sort(): \t\t', timeit.timeit("bubble_sort(orig_list[:])", setup="from __main__ import "
                                                                                          "bubble_sort, orig_list",
                                                       number=1))
print('Lead time bubble_sort_mod(): \t', timeit.timeit("bubble_sort_mod(orig_list[:])", setup="from __main__ import "
                                                                                              "bubble_sort_mod, "
                                                                                              "orig_list", number=1))
print(f'\nОтсортированный массив:\n{bubble_sort_mod(orig_list)}')

"""Улучшил сортировку методом "пузырька." Для этого установил в функцию bubble_sort_mod(lst_obj) flag, 
который принимает только два значения True и False. Замеры времени выполнения функций показали, что данная 
оптимизация наиболее эффективна только если исходный список отсортирован - функция будет возвращать результат сразу 
после первого прохода. 

10 элементов:
Lead time bubble_sort(): 		 3.1200000000009e-05
Lead time bubble_sort_mod(): 	 3.0000000000002247e-05

Lead time bubble_sort(): 		 0.0017268000000000006
Lead time bubble_sort_mod(): 	 0.0018195999999999907

1000 элементов:
Lead time bubble_sort(): 		 0.1964253
Lead time bubble_sort_mod(): 	 0.1923089
"""


# ////////////////////////////////////////////  Task 2  ///////////////////////////////////////////////////////////////

"""2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на 
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы. 

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""


def merge_list(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def merge_sort(s):
    if len(s) == 1:
        return s
    middle = len(s) // 2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_list(left, right)


print('\n\n', 10 * '/', 'Task 2', 10 * '/')
try:
    while True:
        number = int(input('\nВведите число элементов массива: '))
        if number <= 0:
            print('Введите натуральное число!')
        else:
            break

    array = [random.uniform(0, 50) for _ in range(number)]

    print(f'Исходный массив:\n{array}')
    print(f'Отсортированный массив:\n{merge_sort(array[:])}')
    print(f'\nВремя выполнения merge_sort() при {number} элементах массива: ')
    print(timeit.timeit("merge_sort(array[:])", setup="from __main__ import merge_sort, array", number=1))
except ValueError:
    print('Введите натуральное число!')

""" Результаты выполнения:

Время выполнения merge_sort() при 10 элементах массива: 
4.669999999862284e-05

Время выполнения merge_sort() при 100 элементах массива: 
0.0004765000000004349

Время выполнения merge_sort() при 1000 элементах массива: 
0.006249999999999645

Время выполнения merge_sort() при 10000 элементах массива: 
0.004293000000000546

Время выполнения merge_sort() при 100000 элементах массива: 
0.0873759000000005

ВЫВОД:
    Замеры показали, что сортировка методом слияния - оптимальный алгоритм сортировки. 
    Его сложность - O(N logN).
"""


# ////////////////////////////////////////////  Task 3  ///////////////////////////////////////////////////////////////

"""3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. 
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше 
медианы, в другой – не больше медианы. 

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""


def shell_sort(lst):  # сортировка Шелла
    gap = len(lst) // 2

    while gap > 0:
        for value in range(gap, len(lst)):
            current_value = lst[value]
            position = value

            while position >= gap and lst[position - gap] > current_value:
                lst[position] = lst[position - gap]
                position -= gap
                lst[position] = current_value

        gap //= 2
    return lst


def median_shell_sort(lst):  # находим медиану, предварительно отсортировав массив методом Шелла
    i = len(shell_sort(lst)) // 2
    return lst[i]


def median_no_sort(lst):
    med = None
    left = []
    right = []
    identical_values = []  # массив, где будут храниться одинаковые значения из исходного списка
    for i in range(len(lst)):
        for j in range(len(lst)):
            if j != i:
                if lst[j] < lst[i]:
                    left.append(lst[j])
                elif lst[j] > lst[i]:
                    right.append(lst[j])
                else:
                    identical_values.append(lst[j])
        for el in identical_values:  # равномерно распределяем элементы в списки left и right
            if len(left) < len(right):
                left.append(el)
            else:
                right.append(el)
        if len(left) == len(right):
            med = lst[i]
            break
        left.clear()
        right.clear()
        identical_values.clear()

    return med


print('\n\n', 10 * '/', 'Task 3', 10 * '/', '\n')

m = 5
array_size = 2 * m + 1
array = [random.randint(0, 100) for _ in range(array_size)]

print(f'Исходный массив на {array_size} элементов:\n{array}\n')
print(f'Медиана: {median(array[:])}')
print(f'Медиана: {median_no_sort(array[:])}')
print(f'Медиана: {median_shell_sort(array[:])}')
print(f'\nОтсортированный массив:\n{shell_sort(array[:])}\n')

# замеры
print('Lead time median():\t\t\t\t', timeit.timeit("median(array[:])", setup="from __main__ import median, array",
                                                   number=1))
print('Lead time median_shell_sort():\t', timeit.timeit("median_shell_sort(array[:])", setup="from __main__ import "
                                                                                             "median_shell_sort, array",
                                                        number=1))
print('Lead time median_no_sort(): \t', timeit.timeit("median_no_sort(array[:])", setup="from __main__ import "
                                                                                        "median_no_sort, array",
                                                      number=1))

""" Результаты выполнения:

Массив из 11 элементов:
Lead time median():				 3.7999999999982492e-06
Lead time median_shell_sort():	 1.6400000000249548e-05
Lead time median_no_sort(): 	 3.019999999986922e-05

Массив из 101 элемента:
Lead time median():				 1.6000000000016e-05
Lead time median_shell_sort():	 0.00032530000000008386
Lead time median_no_sort(): 	 0.00047140000000034377

Массив из 1001 элемента:
Lead time median():				 0.00012420000000012976
Lead time median_shell_sort():	 0.004962700000000098
Lead time median_no_sort(): 	 0.11631210000000003

ВЫВОД:
    Лучше всего с поиском медианы справляется функция median() из библиотеки statistics. Хуже всего, когда массив не 
    отсортирован - median_no_sort(). Делаю окончательный вывод, если хочешь что-то найти, сперва отсортируй.
"""
