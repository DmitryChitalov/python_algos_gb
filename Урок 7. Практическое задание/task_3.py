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

import numpy, random, timeit

original_lst = [random.randint(0,9) for _ in range(2 * random.randint(2, 9) + 1)]
print(original_lst)

def shell_(oList):
    inc = len(oList) // 2
    while inc:
        for i, el in enumerate(oList):
            while i >= inc and oList[i - inc] > el:
                oList[i] = oList[i - inc]
                i -= inc
            oList[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return oList

print('shell time: ', timeit.timeit('shell_(original_lst[:])', \
                   setup='from __main__ import shell_, original_lst', \
                    number=100))

print(f'median = {numpy.median(original_lst)}')
print(f'my median = {shell_(original_lst[:])[len(original_lst) // 2]}')

# без сортировки
def no_sort(oLst, n=0):
    left = []
    right = []
    tmp = oLst[:]
    a = tmp.pop(n)
    for i in range(len(tmp)):
        if a > tmp[i]:
            left.append(tmp[i])
        else:
            right.append(tmp[i])
    if len(left) != len(right):
        no_sort(oLst, n=n+1)
    else:
        return a

print('no sort time: ', timeit.timeit('no_sort(original_lst[:])', \
                   setup='from __main__ import no_sort, original_lst', \
                    number=100))

print(f'no sort median = {no_sort(original_lst)}')

# не всегда корректно работает no_sort(), не пойму...
# и я не понимаю, почему return a возвращает "None"?
# если вместо return делать print(a), то всё нормально,
# но я не хочу писать print, иначе в замере он вернёт его 100 раз

# По замерам:
# чаще всего Шелл лучше, примерно, в 10 раз.
# Но бывают случаи, когда это не так. Мне пока не удалось выяснить закономерность.