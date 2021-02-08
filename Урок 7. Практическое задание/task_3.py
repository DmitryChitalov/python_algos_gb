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
from statistics import median
from timeit import timeit

m = int(input('Введите натуральное число m, для расчёта массива размером 2m + 1: '))
orig_list = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(f'Original list — {orig_list}')
print(f'Median by "statistics" method — {median(orig_list)}')


def shell_sort(lst_obj_shell):
    final_idx = len(lst_obj_shell) - 1
    step = len(lst_obj_shell) // 2
    while step > 0:
        for i in range(step, final_idx + 1, 1):
            j = i
            diff = j - step
            while diff >= 0 and lst_obj_shell[diff] > lst_obj_shell[j]:
                lst_obj_shell[diff], lst_obj_shell[j] = lst_obj_shell[j], lst_obj_shell[diff]
                j = diff
                diff = j - step
        step //= 2
    return lst_obj_shell


def gnome_sort(lst_obj_gnome):
    i = 1

    while i < len(lst_obj_gnome):
        if not i or lst_obj_gnome[i - 1] <= lst_obj_gnome[i]:
            i += 1
        else:
            lst_obj_gnome[i - 1], lst_obj_gnome[i] = lst_obj_gnome[i], lst_obj_gnome[i - 1]
            if i > 1:
                i -= 1
    return lst_obj_gnome


def gnome_median(lst_obj_gnome):
    return gnome_sort(lst_obj_gnome)[len(lst_obj_gnome) // 2]


def without_sort(lst_obj_ws):
    temp = lst_obj_ws
    left_list = []
    right_list = []
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                left_list.append(temp[j])
            if temp[i] < temp[j]:
                right_list.append([j])
            if temp[i] == temp[j] and i > j:
                left_list.append(temp[j])
            if temp[i] == temp[j] and i < j:
                right_list.append(temp[j])
        if len(left_list) == len(right_list):
            return temp[i]
        left_list.clear()
        right_list.clear()


def another_way(lst_obj_aw):
    temp = lst_obj_aw
    for i in range(len(lst_obj_aw) // 2):
        temp.remove(max(temp))
    return max(temp)


print(f'Sorted list by Shell method — {shell_sort(orig_list)}')
print(f'List median by Shell method — {shell_sort(orig_list)[m]}')
print(f'Sorted list by gnome method — {gnome_sort(orig_list)}')
print(f'List median by gnome method — {gnome_median(orig_list)}')
print(f'List median without sort — {without_sort(orig_list)}')
print(f'List median another way — {another_way(orig_list)}')

print(f'{"*" * 10} Timing {"*" * 10}')
print('Median method — ', timeit('median(orig_list[:])', globals=globals(), number=100))
print('Shell method — ', timeit('shell_sort(orig_list[:])', globals=globals(), number=100))
print('Gnome method — ', timeit('gnome_median(orig_list[:])', globals=globals(), number=100))
print('Without sort — ', timeit('without_sort(orig_list[:])', globals=globals(), number=100))
print('Another way — ', timeit('another_way(orig_list[:])', globals=globals(), number=100))

"""
    На данном примере мы отыскали медиану различными методами: встроенной функцией median,
    из отсортированных (методом Shell и Gnome) массисвов, и из неотсортированных массивов.
    Результаты замеров при разлиных значениях m:
    
    m = 10:
    ********** Timing **********
    Median method —  7.400000000012952e-05
    Shell method —  0.0005020999999998388
    Gnome method —  0.00021429999999966753
    Without sort —  0.002106499999999567
    Another way —  0.00026709999999985357
    
    m = 100
    ********** Timing **********
    Median method —  0.00017000000000022553
    Shell method —  0.005032400000000159
    Gnome method —  0.0014213000000000697
    Without sort —  0.1413534999999997
    Another way —  0.012976700000000285
    
    m = 1000
    ********** Timing **********
    Median method —  0.0009196000000000204
    Shell method —  0.09000560000000002
    Gnome method —  0.015615600000000285
    Without sort —  14.425066400000002
    Another way —  1.0381440000000026
    
    Объективно, наилучший результат даёт встроенный метод median из модуля statistics.
    Худшие значения времени поиска медианы показали методы без сортировки.
"""
