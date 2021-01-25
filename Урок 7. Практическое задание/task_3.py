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
from timeit import timeit


def gnome_sort(lst):
    i = 1
    while i < len(lst):
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    return lst


while True:
    try:
        m = int(input("Введите m: "))
        orig_lst = [randint(0, 100) for _ in range(2 * m + 1)]
        print(gnome_sort(orig_lst))
        print(f'Медианный элемент будет равен {gnome_sort(orig_lst)[m]}')
        print(f'Провверка: {median(orig_lst)}')
        break
    except ValueError:
        print('Вы ввели не число попробуйте еще раз.')


orig_list = [randint(0, 100) for _ in range(2 * 5 + 1)]
print(timeit("gnome_sort(orig_list)", setup="from __main__ import gnome_sort, orig_list", number=100))
orig_list2 = [randint(0, 100) for _ in range(2 * 50 + 1)]
print(timeit("gnome_sort(orig_list2)", setup="from __main__ import gnome_sort, orig_list2", number=100))
orig_list3 = [randint(0, 100) for _ in range(2 * 500 + 1)]
print(timeit("gnome_sort(orig_list3)", setup="from __main__ import gnome_sort, orig_list3", number=100))
