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
""" Пять функций нахождения медианы без сортировки.
 'share' функция содержит мой алгоритм нахождения медианы"""


def median_nature(arr):
    """Функция для проверки результата"""
    return median(arr)


def search_med0(arr):
    """Эта функция как образец для всех остальных"""
    if len(arr) == 2:
        # print(sum(arr)/2)
        return sum(arr)/2
    elif len(arr) ==1:
        # print(*arr)
        return arr[0]
    arr.remove(max(arr))
    arr.remove(min(arr))
    return search_med0(arr)


def search_med1(arr):
    # Принцип функции search_med0
    # Применен 'пузырьковый метод' поиска min, max
    if len(arr) == 2:
        # print(sum(arr)/2)
        return sum(arr)/2
    elif len(arr) == 1:
        # print(*arr)
        return arr[0]

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
    arr.remove(arr[-1])
    for i in range(len(arr)-1, 0, -1):
        if arr[i] < arr[i-1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    arr.remove(arr[0])
    return search_med1(arr)


def search_med2(arr):
    # Применен 'пузырьковый метод' поиска max
    # Одновременно за проход фиксируется min
    if len(arr) == 2:
        return sum(arr)/2
    elif len(arr) == 1:
        return arr[0]
    minimum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
        if arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    arr.remove(arr[-1])
    arr.remove(minimum)
    return search_med2(arr)


def share(test_list, d_l=0, d_r=0):
    """Функция делит массив на 2 части 'больше' 'меньше' относительно случайного
    (первого) элемента до нахождения искомого элемента
    Работает только для нечетного количества элементов """
    left = list()
    right = list()
    test_i = test_list[0]       # элемент основа для деления на два массива

    for i in test_list[1:]:     # Деление на две части больше, меньше
        if i > test_i:
            right.append(i)
        else:
            left.append(i)
    right.append(test_i)        # Основу определяем в правый массив, для избежания зацикливания

    len_left = len(left) + d_l  # Длина (количество элементов) слева + величина изменения
    len_right = len(right) + d_r
    if len_left == (len_right - 1):     # Проверка количества элементов слева и справа от основы деления
        return test_i                   # искомый элемент
    elif len_right > len_left:
        test_list = right       # Отсечение элеменов
        d_l += len(left)        # Вместо удаленныхэлементов: величина измениния 'слева' (здесь)
    else:
        test_list = left
        d_r += len(right)

    return share(test_list, d_l, d_r)


array = [random.randint(0, 10) for _ in range(1101)]

arr1 = array.copy()

print("Идеал", timeit.timeit("median_nature(arr1)", setup="from __main__ import median_nature, arr1", number=1)*1000)
print(arr1)

print("min, max", timeit.timeit("search_med0(arr1)", setup="from __main__ import search_med0, arr1", number=1)*1000)

arr2 = array.copy()
print("Пузырек", timeit.timeit("search_med1(arr2)", setup="from __main__ import search_med1, arr2", number=1)*1000)

arr3 = array.copy()
print("New", timeit.timeit("search_med2(arr3)", setup="from __main__ import search_med2, arr3", number=1)*1000)

arr4 = array.copy()
print("share", timeit.timeit("share(arr4)", setup="from __main__ import share, arr4", number=1)*1000)

arrN = array.copy()
print(median_nature(arrN))
arr00 = array.copy()
print(search_med0(arr00))
arr11 = array.copy()
print(search_med1(arr11))
array22 = array.copy()
print(search_med2(array22))
array33 = array.copy()
print(share(array33))

""" По результатам замеров
Функция share() самая быстрая, так как она отсекает часть массива,
поэтому проходов по элементам меньше.
Умножение на 1000 для визуализации результатов замеров 

Идеал 0.11010000000000186
min, max 22.639899999999997
Пузырек 185.8028
New 145.14560000000003
share 1.3586999999999905
"""
