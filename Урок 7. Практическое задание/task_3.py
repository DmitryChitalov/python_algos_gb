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

# воспользуемся гномьей сортировкой для списка


def gnome_sort(lst, size):
    i = 1
    while i < size:
        if (lst[i - 1] <= lst[i]):
            i += 1
        else:
            tmp = lst[i]
            lst[i] = lst[i - 1]
            lst[i - 1] = tmp
            i -= 1
            if (i == 0):
                i = 1
    return lst

# воспользуемся сортировкой Шелла для списка

def shell(lst):
    inc = len(lst) // 2
    while inc:
        for i, el in enumerate(lst):
            while i >= inc and lst[i - inc] > el:
                lst[i] = lst[i - inc]
                i -= inc
            lst[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return lst


m = int(input('Please, insert m: '))
my_lst = [randint(0, 100) for i in range(2 * m + 1)]

new_lst_1 = gnome_sort(my_lst, len(my_lst))
print(f'Sorted list by gnome method: {new_lst_1}')

median_search_gnome = new_lst_1[len(new_lst_1) // 2]
print(f'The median of gnome sorted list: {median_search_gnome}')


new_lst_2 = shell(my_lst)
print(f'Sorted list by shell method: {new_lst_2}')

median_search_shell = new_lst_2[len(new_lst_2) // 2]
print(f'The median of shell sorted list: {median_search_shell}')

# Проверим методом statistics, правильно ли рассчитана медиана списка:

print('The median calculated by statistics module is: ', median(my_lst))
