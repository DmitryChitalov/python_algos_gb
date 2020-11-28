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

from random import randrange

m = 4
my_list = [randrange(1, 15) for _ in range(2 * m + 1)]
print(my_list)
# Работает не идеально, при дубликарах значения медианы левый и правый массивы формируются не правильно
for i in range(len(my_list)):
    left = [j for j in my_list if j < my_list[i]]
    right = [k for k in my_list if k > my_list[i]]
    if len(left) == len(right):
        print(f'медиана {my_list[i]}')
        break


def decoratort(func):
    def foo(lst):
        func(lst)
        return f'{lst}\nмедиана {lst[m - 1]}'

    return foo


@decoratort
def shell_sort(lst):
    sub_list_count = len(lst) // 2
    while sub_list_count > 0:

        for start_position in range(sub_list_count):
            gap_insertion_sort(lst, start_position, sub_list_count)

        sub_list_count = sub_list_count // 2
    return lst


def gap_insertion_sort(lst, start, gap):
    for i in range(start + gap, len(lst), gap):

        current_value = lst[i]
        position = i

        while position >= gap and lst[position - gap] > current_value:
            lst[position] = lst[position - gap]
            position = position - gap

        lst[position] = current_value


print(shell_sort(my_list[:]))
