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


def gnome_sort(list_obj):
    i = 1
    size = len(list_obj)
    while i < size:
        if list_obj[i - 1] <= list_obj[i]:
            i += 1
        else:
            list_obj[i], list_obj[i - 1] = list_obj[i - 1], list_obj[i]
            i -= 1
            if i == 0:
                i = 1
    return list_obj


def get_list_median(list_obj, m):
    return gnome_sort(list_obj)[m]


if __name__ == "__main__":
    m = 50
    test_list = [random.randint(0, 100) for i in range(2 * m + 1)]
    print(median(test_list[:]))
    print(get_list_median(test_list[:], m))
    print('Профилировка времени гномьей сортировки')
    print(timeit(
        "gnome_sort(test_list[:])",
        setup="from __main__ import gnome_sort, test_list", number=1000)
    )

"""
Выводы: Гномья сортировка обладает худшей эффективностью по времени в сравнении с пузырьковой сортировкой
и сортировкой слиянием.
"""