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
from random import randint
from statistics import median


# Без сортировки
def my_median(lst):
    return median(lst)


# Сортировка
def gnome_sort(my_list):
    i = 1
    j = 2
    a = my_list.copy()
    while i < len(a):
        if a[i - 1] > a[i]:
            i = j
            j = j + 1
        else:
            a[i - 1], a[i] = a[i], a[i - 1]
            i = i - 1
            if i == 0:
                i = j
                j = j + 1
    return a


number = int(input('Введите натуральное число: '))
orig_list = [randint(1, 100) for _ in range(number*2+1)]
sort_list = gnome_sort(orig_list)
print(f'Оригинальный список:  \n{orig_list}')
print(f'Отсортированный список:  \n{sort_list}')
median_ind = len(sort_list) // 2
sorted_median = sort_list[median_ind]
print('Медиана без сортировки: \n', my_median(orig_list))
print(f'Медиана после сортировки:  \n {sorted_median}')



