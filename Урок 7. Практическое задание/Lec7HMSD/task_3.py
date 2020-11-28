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

import timeit
import random
from statistics import median


def my_median(ls):
    o = 1
    res = 0

    for i in range(col):
        k = 0
        r = 0
        for j in range(col):
            if ls[j] <= ls[i]:
                k += 1
            if ls[j] >= ls[i]:
                r += 1
        #    print(orig_list[i], "k=", k, "r=", r, abs(1-k/r),  abs(1-r/k))
        kr = abs(1 - k / r)
        rk = abs(1 - r / k)
        if kr < o:
            res = ls[i]
            o = kr
        if rk < o:
            res = ls[i]
            o = rk
        if o == 0: break
    return res


def my_median2(ls):
    for i in range(col):
        k = 0
        r = 0
        for j in range(col):
            if ls[j] <= ls[i]:
                k += 1
            if ls[j] >= ls[i]:
                r += 1
        # print(orig_list[i], "k=", k, "r=", r, k-r,  r-k)
        if abs(k - r) <= 1: break
    return ls[i]


def shell_sort(ls):
    trigger = len(ls) // 2
    while trigger:
        for i, el, in enumerate(ls):
            while i >= trigger and ls[i - trigger] > el:
                ls[i] = ls[i - trigger]
                i -= trigger
            ls[i] = el
        trigger = 1 if trigger == 2 else int(trigger * 5.0 / 11)
    res = ls[len(ls) // 2]
    return res


col = 15
orig_list = [random.randint(1, 100) for _ in range(col)]

print(my_median(orig_list))
print(my_median2(orig_list))
print(median(orig_list))
print(shell_sort(orig_list[:]))
print(orig_list)

print(timeit.timeit("my_median(orig_list[:])", \
                    setup="from __main__ import my_median, orig_list", number=10000))

print(timeit.timeit("my_median2(orig_list[:])", \
                    setup="from __main__ import my_median2, orig_list", number=10000))

print(timeit.timeit("shell_sort(orig_list[:])", \
                    setup="from __main__ import shell_sort, orig_list", number=10000))

print(timeit.timeit("median(orig_list[:])", \
                    setup="from __main__ import median, orig_list", number=10000))

# Попытался решить без сортировки. Кажется получилось.
# Идея - частное от кол-во элементом не больше и не меньше медианы стремится к нулю.
# И вторая идея, что разница кол-во элементов >= и <= по модулю всегда 1 или 0. (Этот вариант чуть быстрее)
# Но эта идея оказалась слишком медленной. Уверен что можно ещё оптимизировать, но слишком поздно начал делать(
# При варианте когда все элементы массива уникальны, моя функция быстрее (см второй снимок результатов ниже).

# 61
# 61
# 61
# 61
# [50, 7, 56, 92, 73, 33, 39, 95, 82, 74, 62, 91, 61, 42, 38]
# 0.7749986
# 0.7101153
# 0.17078039999999994
# 0.00876560000000004

# 36
# 36
# 36
# 36
# [90, 30, 77, 36, 87, 59, 1, 31, 5, 3, 84, 78, 7, 54, 27]
# 0.2352165
# 0.2744414
# 0.31152139999999995
# 0.015695099999999962
