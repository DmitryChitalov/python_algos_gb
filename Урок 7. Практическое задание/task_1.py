"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
from random import randint
from timeit import timeit


def bubble_sort(var_list):
    n = 1
    while n < len(var_list):
        for i in range(len(var_list) - n):
            if var_list[i] < var_list[i + 1]:
                var_list[i], var_list[i + 1] = var_list[i + 1], var_list[i]
        n += 1
    return var_list


def bubble_sort_2(var_list):
    n = 1
    zamena = False
    while n < len(var_list):
        zamena = False
        for i in range(len(var_list) - n):
            if var_list[i] < var_list[i + 1]:
                var_list[i], var_list[i + 1] = var_list[i + 1], var_list[i]
                zamena = True
        if zamena == False:
            break
        n += 1
    return var_list


def bubble_sort_3(var_list):
    n = 1
    zamena = False
    while n < len(var_list):
        zamena = False
        for i in range(len(var_list) - n):
            if var_list[i] < var_list[i + 1]:
                var_list[i], var_list[i + 1] = var_list[i + 1], var_list[i]
                zamena = True
                j = i
                while j > 1 and var_list[j] > var_list[j - 1]:
                    var_list[j], var_list[j - 1] = var_list[j - 1], var_list[j]
                    j = j - 1
        if zamena == False:
            return var_list
        n += 1
    return var_list

orig_list = [randint(-100, 100) for _ in range(10)]

# замеры 10
print()
print(f'замеры 10')
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "bubble_sort_2(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "bubble_sort_3(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]
# замеры 100
print()
print(f'замеры 100')
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "bubble_sort_2(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "bubble_sort_3(orig_list[:])",
        globals=globals(),
        number=1000))

# замеры 1000
orig_list = [randint(-100, 100) for _ in range(1000)]
print()
print(f'замеры 1000')
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "bubble_sort_2(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "bubble_sort_3(orig_list[:])",
        globals=globals(),
        number=1000))

#
# замеры 10
# 0.0208719
# 0.01814189999999999
# 0.017113099999999992
#
# замеры 100
# 1.5631929000000002
# 1.4333779
# 1.2376698000000004
#
# замеры 1000
# 148.0967632
# 153.81954240000002
# 132.64034569999995
#
#
# во второй реализации выходим если не было перестановок
#  в третьей реализации также добавил, что если меняем местами элементы, то
# сравниваем с предыдущими пока он не встанет на место (возможно это уже и не
# сортировка пузырьком)
# скрость выполнения второй реализации зависит от изначального массива.
# Если он отсортирован, то выполняется гораздо быстрее
# третья реализация выпоняется быстрее

