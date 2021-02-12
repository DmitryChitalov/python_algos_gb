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


def get_gvg_md(i_lst):
    l_max_val = int((len(i_lst) - 1)/2)
    for i in range(len(i_lst)):
        l_left_cnt = 0
        l_righ_cnt = 0
        for j in range(len(i_lst)):
            if i == j:
                continue
            if i_lst[j] <= i_lst[i] and l_left_cnt < l_max_val:
                l_left_cnt += 1
            elif i_lst[j] >= i_lst[i] and l_righ_cnt < l_max_val:
                l_righ_cnt += 1
        #print(i, i_lst[i], l_left_cnt, l_righ_cnt)
        if l_left_cnt == l_righ_cnt:
            return i_lst[i]
    return None


m = 5
g_lst = [randint(1, 50) for i in range(2*m + 1)]
print(g_lst)
print('Median from statistics:', median(g_lst))
print('Median from get_gvg_md:', get_gvg_md(g_lst))
