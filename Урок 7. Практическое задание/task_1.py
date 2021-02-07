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
import timeit

orig_list = [randint(-100, 100) for _ in range(10)]


def bubble_find_max(array):
    a = False
    i = 0
    while a & i < len(array) - 1:
        if i != len(array) - 1:
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                a = True
            i += 1
        else:
            if not a:
                break
            else:
                i = 0
                a = False
    return array


def bubble_sort(lst_obj):
    a = False
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                a = True
        if not a:
            break
        else:
            n += 1
            a = False

    return lst_obj


def bubble_sort_norm(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


print(orig_list)
print(bubble_find_max(orig_list[:]))
print(bubble_sort_norm(orig_list[:]))
print(bubble_sort(orig_list[:]))

# замеры 10
print(
    timeit.timeit(
        "bubble_find_max(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_norm(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "bubble_find_max(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_norm(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "bubble_find_max(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_norm(orig_list[:])",
        globals=globals(),
        number=1000))

'''
Сделал вначале свою пузырьковую сортировку но она значительно медленнее по замерам оказалась чем оригинальная,
ну потому что у меня моя сортировка все время по всей длинне списка бегает а в оригинальной длинна списка
после каждой итерации уменьшается на последний отсортированный объект.
Улучшение с прерыванием если список уже отсортирован сделал, но реально он улучшает время только если список на
вход поступает уже отсортированным ну или частично отсортирован, на рандомных списках показатели изменились 
незначительно

0.03198259200000003
0.00959103
0.011286645999999956
2.670668718
0.79603943
0.7180229830000004
388.717602386
87.457910647
87.125186268

'''