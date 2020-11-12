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
from random import randint, randrange
from statistics import median
from timeit import timeit

m = int(input('Введите натуральное число: '))

# в массиве user_lst ищем медиану без сортировки, затем с сортировкой Шелла
user_lst = [randint(-10, 10) for _ in range(2 * m + 1)]

# делаем копию user_lst, чтобы работать с неизмененной после сортировки Шелла версией. Будем сортировать его HeapSort
user_lst1 = user_lst.copy()

# для тестирования времени при поиске медианы через алгоритмы сортировки
user_lst_test1 = user_lst.copy()
user_lst_test2 = user_lst.copy()

print(user_lst)  # исходный массив до сортировки
print(f'Медиана для данного массива: {median(user_lst)} (проверка from statistics import median)')


# Вариант с поиском медианы без сортировки (честно нагуглил и немного переделал)
def Partition(arr, l, r):
    """Возвращает позицию осевого элемента"""
    lst = arr[r]
    i = l
    j = l
    while j < r:
        if arr[j] < lst:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

        j += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i


def randomPartition(arr, l, r):
    n = r - l + 1
    pivot = randrange(1, 100) % n
    arr[l + pivot], arr[r] = arr[r], arr[l + pivot]
    return Partition(arr, l, r)


def MedianUtil(arr, l, r, k, a1, b1):
    global a, b

    # if l < r
    if l <= r:

        # Find the partition index
        partition_index = randomPartition(arr, l, r)

        # If partion index = k, then
        # we found the median of odd
        # number element in arr[]
        if partition_index == k:
            b = arr[partition_index]
            if a1 != -1:
                return

        # If index = k - 1, then we get
        # a & b as middle element of
        # arr[]
        elif partition_index == k - 1:
            a = arr[partition_index]
            if b1 != -1:
                return

        # If partition_index >= k then
        # find the index in first half
        # of the arr[]
        if partition_index >= k:
            return MedianUtil(arr, l, partition_index - 1, k, a, b)

        # If partition_index <= k then
        # find the index in second half
        # of the arr[]
        else:
            return MedianUtil(arr, partition_index + 1, r, k, a, b)

    return


# Function to find Median
def findMedian(arr, n):
    global a
    global b
    a = -1
    b = -1

    # В нашем случае длина массива всегда нечетное число
    if n % 2 == 1:
        MedianUtil(arr, 0, n - 1, n // 2, a, b)
        res = b
    print(f'Медиана для данного массива: {res} (вычисленная функцией поиска медианы без сортировки)')


findMedian(user_lst, len(user_lst))


# Вариант с поиском медианы c сортировкой Шелла
def shellSort(some_list):
    sublist_count = len(some_list) // 2
    while sublist_count > 0:

        for start_position in range(sublist_count):
            gapInsertionSort(some_list, start_position, sublist_count)

        sublist_count = sublist_count // 2


def gapInsertionSort(some_list, start, gap):
    for i in range(start + gap, len(some_list), gap):

        current_value = some_list[i]
        position = i

        while position >= gap and some_list[position - gap] > current_value:
            some_list[position] = some_list[position - gap]
            position = position - gap

        some_list[position] = current_value


shellSort(user_lst)
print(f'Медиана для данного массива: {user_lst[m]} (с сортировкой Шелла)')


# Вариант с поиском медианы c сортировкой кучей
def heapify(some_list, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and some_list[i] < some_list[l]:
        largest = l

    if r < n and some_list[largest] < some_list[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        some_list[i], some_list[largest] = some_list[largest], some_list[i]
        heapify(some_list, n, largest)


def heapSort(some_list):
    n = len(some_list)

    # Build max heap
    for i in range(n // 2, -1, -1):
        heapify(some_list, n, i)

    for i in range(n - 1, 0, -1):
        # Swap
        some_list[i], some_list[0] = some_list[0], some_list[i]

        # Heapify root element
        heapify(some_list, i, 0)


heapSort(user_lst1)

print(f'Медиана для данного массива: {user_lst1[m]} (с сортировкой HeapSort)')
print('-' * 160)

print('Время поиска медианы с помощью сортировки Шелла: ', timeit(
    'shellSort(user_lst_test1)',
    setup='from __main__ import gapInsertionSort, shellSort, user_lst_test1',
    number=1
))
print('-' * 160)
print('Время поиска медианы с помощью сортировки HeapSort: ', timeit(
    'heapSort(user_lst_test2)',
    setup='from __main__ import heapSort, heapify, user_lst_test2',
    number=1
))

"""Сортировка Шелла отрабатывет быстрее сортировки кучей"""
