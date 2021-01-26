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
import timeit
import copy
from statistics import median

m = random.randint(0, 5)
my_lst = [random.randint(-50, 50) for _ in range(2 * m + 1)]
copy_my_lst = copy.copy(my_lst)
copy_my_lst_2 = copy.copy(my_lst)

print(my_lst)

# использование встроенной функции
print(median(my_lst))


# с сортировкой
def my_sort(lst_obj):
    new_list = lst_obj
    left = []
    right = []
    for i in range(len(new_list)):
        for j in range(len(new_list)):
            if new_list[i] == new_list[j] and i > j:
                left.append(new_list[j])
            elif new_list[i] == new_list[j] and i < j:
                right.append(new_list[j])
            elif new_list[i] > new_list[j]:
                left.append(new_list[j])
            elif new_list[i] < new_list[j]:
                right.append(new_list[j])
        if len(left) == len(right):
            return new_list[i]
        left.clear()
        right.clear()


print(my_sort(copy_my_lst))


# без сортировки
def my_sort_2(lst_obj):
    new_list = lst_obj
    for i in range(len(new_list) // 2):
        new_list.remove(max(new_list))
    return max(new_list)


print(my_sort_2(my_lst))


## Время:
print(timeit.timeit("median(my_lst)", setup = "from __main__ import median, my_lst", number = 10000))

print(timeit.timeit("my_sort(copy_my_lst)", setup = "from __main__ import my_sort, copy_my_lst", number = 10000))

print(timeit.timeit("my_sort_2(copy_my_lst_2)", setup = "from __main__ import my_sort_2, copy_my_lst_2", number = 10000))


"""
Результаты:

median = 0.015181212998868432
my_sort = 0.5306191989984654
my_sort_2 = 0.061818566000511055

Из результатов видно, что встроенная функция работает быстрее остальных.
"""