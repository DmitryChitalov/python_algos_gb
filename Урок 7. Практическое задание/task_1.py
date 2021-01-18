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
from timeit import timeit
from random import randint
from task_2 import my_sort #, merger


def buble_1(arr):
    i = 0
    while i < len(arr):
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]  # это какой-то неправильный пузырек... Но сортирует
        i += 1
    return arr


def buble_2(arr):
    i = 0
    while i < len(arr):
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # а это правильный пузырек
        i += 1
    return arr


def buble_3(arr):  # нагло используем подсказку про лишние проходы
    i = 0
    flag = 1
    while i < len(arr):
        flag = 0
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag += 1
        if flag == 0:
            break
        i += 1
    return arr  # , i


def buble_4(arr):
    i = 0
    arr_len = len(arr)
    while i < arr_len:
        flag = 0
        for j in range(arr_len):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                flag += 1
            # if arr[arr_len - 1 - i] < arr[arr_len - 1 - j]:
            #     arr[arr_len - 1 - i], arr[arr_len - 1 - j] = arr[arr_len - 1 - j], arr[arr_len - 1 - i]
            #     flag += 1
        if flag == 0:
            break
        i += 1
    return arr

def get_arr(l):
    return [randint(-100, 100) for i in range(l)]


if __name__ == '__main__':
    my_arr = get_arr(100)
    print(my_arr)
    print(buble_1(my_arr[:]))
    print(buble_2(my_arr[:]))
    print(buble_3(my_arr[:]))
    print(timeit('buble_1(my_arr[:])',
                 setup='from __main__ import buble_1, my_arr',
                 number=1000))
    print(timeit('buble_2(my_arr[:])',
                 setup='from __main__ import buble_2, my_arr',
                 number=1000))
    print(timeit('buble_3(my_arr[:])',
                 setup='from __main__ import buble_3, my_arr',
                 number=1000))
    """
    0.7624581
    0.9749522999999999
    Странно, но неправильный  пузырек работает чуть быстрее чем правильный
    Очевидно что проблема в смене элементов
    """
    """  
    0.7640137
    0.9884670000000001
    0.9398929 -- оптимизированный вариант, как правило отбрасывается несколько последних проходов, поэтому чуть быстрее   
    """
    print(buble_4(my_arr[:]))
    print(timeit('buble_4(my_arr[:])',
                 setup='from __main__ import buble_4, my_arr',
                 number=1000))
    """
    0.7689546999999997
    Четвертый вариант быстрее тру-пузырьков, но медленнее первого. И количество проходов всегда равно размеру массива. 
    Поэтому и медленнее - количество операций всегда полное, а дополнительные операции с флагом появляются.
    """
    # print(my_sort(my_arr[:]))
    # print(timeit('my_sort(my_arr[:])',
    #              setup='from __main__ import my_sort, my_arr',
    #              number=1000))

    """ 
    0.21296840000000028
    Просто чтоб сравнить с сортировкой слиянием из второго примера. Она существенно быстрее
    """
