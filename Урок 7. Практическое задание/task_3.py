"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]
"""
from random import randint
from statistics import median
import timeit


def without_sort(lst_obj):
    temp = lst_obj
    left_list = []
    right_list = []
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                left_list.append(temp[j])
            if temp[i] < temp[j]:
                right_list.append(temp[j])
            if temp[i] == temp[j] and i > j:
                left_list.append(temp[j])
            if temp[i] == temp[j] and i < j:
                right_list.append(temp[j])
        if len(left_list) == len(right_list):
            return temp[i]
        left_list.clear()
        right_list.clear()


def another_way(lst_obj):
    """
    Возвращаем медиану массива путем удаления максимальных элементов
    """
    temp_list = lst_obj
    for i in range(len(lst_obj) // 2):
        temp_list.remove(max(temp_list))
    return max(temp_list)


def gnome_sort(sort_list):
    """
    Сортировка списка методом gnome_sort
    Происходит просмотр массива слева-направо,
    при этом сравниваются (и меняются, если неотсортированная пара) соседние элементы,
    Если происходит обмен элементов, то происходит возвращение на один шаг назад.
    Если обмена не происходит, то алгоритм продолжает просмотр массива слева-направо в
    поиске неотсортированных пар.
    """
    i = 1
    while i < len(sort_list):
        if not i or sort_list[i - 1] <= sort_list[i]:
            i += 1
        else:
            sort_list[i], sort_list[i - 1] = sort_list[i - 1], sort_list[i]
            i -= 1
    return sort_list


# def gnome_median(sort_list):
#     return gnome_sort(sort_list)[len(sort_list) // 2]


m = int(input('Input m: '))
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
# print(f'Исходный массив:\n{orig_list}\n')

# Нахождение медианы через встроенную функцию
print(f'Медиана, ф-я median -  {median(orig_list)}')
# Нахождение медианы без сортировки исходного массива
print(f'Медиана (без сортировки), while - {without_sort(orig_list)}')
# Нахождение медианы еще одним вариантом без сортировки исходного массива
print(f'Медиана (без сортировки), нахождение max - {another_way(orig_list)}')
# Нахождение медианы с сортировкой исходного массива
print(f'Медиана (c сортировкой), гномья - {gnome_sort(orig_list)[m]}')



# orig_list10 = [randint(0, 100) for i in range(2 * m + 1)]

# замеры 100000
print('median', timeit.timeit(
    "median(orig_list[:])",
    globals=globals(),
    number=100000))

print('while', timeit.timeit(
    "without_sort(orig_list[:])",
    globals=globals(),
    number=100000))

print('max', timeit.timeit(
    "another_way(orig_list[:])",
    globals=globals(),
    number=100000))

print('gnome', timeit.timeit(
    "gnome_sort(orig_list[:])",
    globals=globals(),
    number=100000))

"""
m = 5
number = 10000

median 0.004411900000000024
while 0.07135729999999985
max 0.010538099999999773
gnome 0.005991800000000325  
___________________________________
m=50
number = 100000

median 0.06234460000000008
while 19.8066279
max 1.824210400000002
gnome 0.41505090000000067 

Вывод: медиану быстрее всего находит встроенная ф-я median, затем ф-я гномья. 3-я по скорости - ф-я max внутри
another_way. Цикл while использовать нельзя, слишком долгая.
"""