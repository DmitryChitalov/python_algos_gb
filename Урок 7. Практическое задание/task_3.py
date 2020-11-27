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



def gnome(lst):
    # standard realisation of Gnome sorting algorithm
    i, size = 1, len(lst)
    while i < size:
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    return lst


def med(lst):
    # standard code for median finding
    lst = gnome(lst)
    if len(lst) % 2 == 1:
        return lst[len(lst) // 2]
    else:
        return 0.5 * (lst[len(lst) // 2 - 1] + lst[len(lst) // 2])


# m as a random integer:
m = randint(1, 25)

# list via using m in list length:
my_list = [randint(1, 100) for i in range(2 * m + 1)]

# results:
print(my_list)
print(gnome(my_list))
print(med(my_list))

# check:
print(median(my_list))