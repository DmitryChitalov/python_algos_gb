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
from timeit import timeit
from statistics import median
from random import randint

#1 Гномья


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

def median(lst:list):
    return gnome(lst)[len(lst) // 2]

m = int(input('Введите кол-во элементов'))
data = [randint(0, 50) for i in range(2*m+1)]
print(data)
print(gnome(data))
print(median(gnome(data)))

print('median(gnome(data)))', timeit('median(gnome(data))', setup='from __main__ import median, gnome, data'))
# время выполнения 3.4959716

#2
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


print(without_sort(data))

print('without_sort(data)', timeit('without_sort(data)', setup='from __main__ import without_sort, data'))
#разобрала поиск медианы в несортированном списке. Интересно, но очень долго. Замеры  - 40.0596. Наглядно видна скорость
# механизмов работы со списками в отличии от мануальных методов.