"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import random, randint
from timeit import timeit

# Это декоратор для замеров времени и памяти
from timememit import timememit


# Сначала реализуем функцию слияния двух соседних
# подмассивов внутри большого массива
# r -- массив
# beg -- индекс начала первого массива
# mid -- индекс конца первого масива и начала второго
# end -- индекс конца второго массива
def mergemem(r, beg, mid, end):
    # память выделяется здесь
    a = r[beg:mid]
    b = r[mid:end]
    lena = len(a)
    lenb = len(b)
    ia, ib = 0, 0
    ir = beg
    while True:
        if a[ia] < b[ib]:
            r[ir] = a[ia]
            ia += 1
            ir += 1
            if ia == lena:
                r[ir:ir + lenb - ib] = b[ib:lenb]
                break
        else:
            r[ir] = b[ib]
            ib += 1
            ir += 1
            if ib == lenb:
                r[ir:ir + lena - ia] = a[ia:lena]
                break


# К этому интерфейсу можно адаптировать фрагмент
# функции из конспекта
def mergelect(lst_obj, beg, mid, end):
    left = lst_obj[beg:mid]
    right = lst_obj[mid:end]

    i, j, k = 0, 0, beg

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst_obj[k] = left[i]
            i += 1
        else:
            lst_obj[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        lst_obj[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        lst_obj[k] = right[j]
        j += 1
        k += 1
    return None


# Реализуем функцию, которая будет рекурсивно сортировать,
# в конце вызывая функцию слияния, полученную в качестве
# параметра
def mergesort(a, beg=0, end=-1, mergefun=mergemem):
    if end < 0:
        beg = 0
        end = len(a)
    diff = end - beg
    if diff < 2:
        return None
    half = diff//2
    mid = beg + half
    # оптимизация самого частого случая
    if diff == 2:
        if a[beg] > a[mid]:
            a[beg], a[mid] = a[mid], a[beg]
        return None
    mergesort(a, beg, mid, mergefun)
    mergesort(a, mid, end, mergefun)
    mergefun(a, beg, mid, end)


# Для сравнения используем пример из конспекта
def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        # Здесь выделяется память
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


# Упростим запуск измерений с различными параметрами
def test_sort(size, nruns):
    global arr
    arr = [randint(1000, 9999) for _ in range(size)]

    print('оригинальные сортировка и слияние: ', timeit(
        "a = arr[:]; mergesort(a)",
        globals=globals(), number=nruns))

    print(
        'оригинальная сортировка, слияние из конспекта: ',
        timeit(
            "a = arr[:]; mergesort(a, mergefun=mergelect)",
            globals=globals(), number=nruns))

    print('пример из конспекта', timeit(
        "a = arr[:]; merge_sort(a)",
        globals=globals(), number=nruns))

    print('встроенная функция', timeit(
        "a = arr[:]; a.sort()",
        globals=globals(), number=nruns))


# test_sort(1000, 100)
# ---
# оригинальные сортировка и слияние:  0.1758444319711998
# оригинальная сортировка, слияние из конспекта:  0.23253241798374802
# пример из конспекта 0.25738181499764323
# встроенная функция 0.007573371985927224
# ---
# Сравним с пузырьком
# python task_1.py
# ---
# 6.638946379069239
# ---

test_sort(10000, 10)
# ---
# оригинальные сортировка и слияние:  0.2432736890623346
# оригинальная сортировка, слияние из конспекта:  0.3292464029509574
# пример из конспекта 0.3471352079650387
# встроенная функция 0.013397364993579686
# ---
# Сравним с пузырьком
# python task_1.py
# ---
# 66.67357723996975
# ---

# Можно сделать вывод, что наиболее эффективно
# оптимизации работают в рекурсивной функции,
# когда удается сократить число вызовов.
# Оптимизация функции слияния дает существенно
# меньший выигрыш производительности.


# Теперь проверим реализацию слияния in-place, которая
# не выделяет дополнительной памяти
def merge(a, beg, mid, end):
    while True:
        if a[beg] < a[mid]:
            beg += 1
        else:
            tmp = a[mid]
            # Возможно этот цикл  ...
            for i in range(mid + 1, end):
                if a[beg] < a[i]:
                    break
            else:
                i = end
            #  ... вместе с этим копированием дают O(n^2)
            a[mid:i - 1] = a[mid + 1:i]
            a[i - 1] = a[beg]
            a[beg] = tmp
            beg += 1
        if beg == mid:
            break


arr = [randint(1000, 9999) for _ in range(30000)]


@timememit
def with_merge():
    a = arr[:]
    mergesort(a)


@timememit
def with_merge_inplace():
    a = arr[:]
    mergesort(a, mergefun=merge)


with_merge()
# ---
# with_merge: 0.2094 s, 0.515625 MiB
# ---

with_merge_inplace()
# ---
# with_merge_inplace: 16.4028 s, 0.515625 MiB
# ---

# Мы видим, что память в python выделяется очень
# эффективно, поэтому inplace-сортировка слиянием
# не приносит заметного выигрыша в потреблении памяти,
# однако очень сильно ухудшает производительность
