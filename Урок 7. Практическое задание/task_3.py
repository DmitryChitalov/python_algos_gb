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
import timeit

# m = int(input('Введите м: '))
m = 100
orig_list = [random.randint(-30, 30) for _ in range(2*m + 1)]
orig_list_1 = orig_list.copy()
orig_list_2 = orig_list.copy()
orig_list_3 = orig_list.copy()
print(orig_list)


def median_1(lst):
    a = int((len(lst)-1)/2)
    for i in range(a):
        lst.remove(max(lst))
        lst.remove(min(lst))
    return lst[0]


def median_2(lst):
    a = int((len(lst)-1)/2)
    for i in range(a):
        lst.remove(max(lst))
    med = max(lst)
    return med


print(median(orig_list))
print(median_1(orig_list_1))
print(median_2(orig_list_2))


print(timeit.timeit("median(orig_list)", \
     setup="from __main__ import median, orig_list", number=100))
print(timeit.timeit("median_1(orig_list_1)", \
     setup="from __main__ import median_1, orig_list_1", number=100))
print(timeit.timeit("median_2(orig_list_2)", \
     setup="from __main__ import median_2, orig_list_2", number=100))

# Вот, мой вариант реализации поиска медианы без сортировки (median_1). Для сравнения взяла встроеную функцию (median)
# и еще захотела поэксперементировать и сделала (median_2). Все функции дают одинаковый результат.
# Сделала замеры по времени:
# 7.390000000000174e-05
# 7.690000000000474e-05
# 9.399999999999686e-05
# или:
# 6.090000000000262e-05
# 7.590000000000374e-05
# 9.050000000000724e-05
# Моя основная функция 1 получилась не сильно хуже встроенной! А вот функция 2 оказалось самой неудачной.
# Но я не понимаю, почему. я ведь ущла от лишнего remove(min(lst)) в цикле, а вместо него добавилась только max(lst)


# Решила попробовать и через сортировк. Сам скрипт гномьей сортировки взяла из интернета:

def gnome(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data


# Моя версия поиска медиана через гномью сортировку. В сортировке ничего не меняла,
# просто подогнала под более привычный для меня вид.

def median_gnome(lst):
    i = 1
    while i < len(lst):
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    med_i = int((len(lst)-1)/2)
    return lst[med_i]


# print(median_gnome(orig_list_3))
print(timeit.timeit("median_gnome(orig_list_3)", \
     setup="from __main__ import median_gnome, orig_list_3", number=100))

# По результатам замеров видно, что гномий вариант уступает по времени 1ому варианту буз сортировки.
# 7.489999999998886e-05
# 7.659999999999612e-05
# 0.0001310000000000061
# 0.0002117000000000091
