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
import statistics
from timeit import timeit

m=5 #int(input('Введите кол-вл элементов'))
any_lst = [random.randint(0, 100) for i in range(2*m+1)]
print(any_lst)

def cocktail_sort(lst_obj):
    left = 0
    right = len(lst_obj) - 1
    while left <= right:
        for i in range(left, right):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        right -= 1
        for i in range(right, left, -1):
            if lst_obj[i-1] > lst_obj[i]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
        left += 1
    return lst_obj

def med_search(lst):
    return lst[len(lst) // 2]


print(cocktail_sort(any_lst))

print(med_search(cocktail_sort(any_lst)))

print( 'Check median data', statistics.median(cocktail_sort(any_lst)))

print('coctailsort - ', timeit('med_search(cocktail_sort(any_lst))', setup='from __main__ import med_search, cocktail_sort, any_lst'))

#11.1026001, Вариант с шейкером времязатратный, не оптимальный

#2 Гномья

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

print(gnome(any_lst))

print(med_search(gnome(any_lst)))

print( 'Check median data', statistics.median(gnome(any_lst)))

print('gnomesort - ', timeit('med_search(gnome(any_lst))', setup='from __main__ import med_search, gnome, any_lst'))
# 2.01305999993, по сравнению с шейкером Гномья в примерно 5 раз быстрее, что делает ее более оптимальной для исп-я
#  в данном задании

#3 разобрала пример с урока

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

print('Median search in unsorted list', timeit('without_sort(any_lst)', setup='from __main__ import without_sort, any_lst'))
#38.4488225 - рекордное время...квадратичная слодность дает о себе знать. Но интересно.