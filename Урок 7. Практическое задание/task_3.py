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


def find_median(lst_obj):
    for i in range(len(lst_obj)):
        more = 0
        less = 0
        equal = 0
        new_lst = lst_obj.copy()
        new_lst.pop(i)
        for item in new_lst:
            if item < lst_obj[i]:
                less += 1
            elif item > lst_obj[i]:
                more += 1
            else:
                equal += 1
        if abs(more - less) <= equal:
            return lst_obj[i]
        # 1 2 2  x 4  5 4 7 6 5 6
m = randint(3, 10)
lst = [randint(0, 100) for i in range(2*m + 1)]
print(lst)
result = find_median(lst)
print(result)
print('Значение верно' if median(lst) == result else 'Ошибка')
