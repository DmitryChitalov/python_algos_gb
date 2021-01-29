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
import timeit
from statistics import median


def time_dif(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args)
        print(f"Time to complete function {func.__name__} is: {time.time() - start_time}")
    return wrapper


#Сортировка Шелла
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2


#В конце сортируем вставкой
def gapInsertionSort(blist, start, gap):
    for i in range(start+gap, len(blist), gap):
        currentvalue = blist[i]
        position = i
        while position >= gap and blist[position-gap] > currentvalue:
            blist[position] = blist[position-gap]
            position = position-gap
        blist[position] = currentvalue


def lcl_median_sorted(lcl_lst=[]):
    return lcl_lst[int(len(lcl_lst) / 2)]


def lcl_median(lcl_lst=[]):
    lower = 0
    for i in range(len(lcl_lst)):
        for j in range(len(lcl_lst)):
            if lcl_lst[i] >= lcl_lst[j]:
                lower += 1
        if lower == int(len(lcl_lst) / 2 + 1) or lcl_lst.count(lcl_lst[i]) >= int(len(lcl_lst) / 2):
            return lcl_lst[i]
        else:
            lower = 0


orig_list = [random.randint(-100, 100) for _ in range(11)]
print(f"Исходный неотсортированный массив: {orig_list}")
lst = sorted(orig_list)
print(f"Отсортированный массив: {lst}")
print(f"Медиана из statistics: {median(orig_list)}")
print(f"Медиана моя для несортированного массива: {lcl_median(orig_list)}")
print(f"Исходный неотсортированный массив: {orig_list}")
shellSort(orig_list)
print(f"Отсортированный массив методом Шелла: {orig_list}")
print(f"Медиана моя для сортированного массива: {lcl_median_sorted(orig_list)}")
print('*'*18 + 'Нестандартные случаи:' + '*'*18)
print(f"Медиана моя для несортированного массива [3, 3, 3, 3, 3, 4, 5]: {lcl_median([3, 3, 3, 3, 3, 4, 5])}")
print(f"Медиана моя для несортированного массива [3, 2, 5, 5, 5, 5, 5]: {lcl_median([3, 2, 5, 5, 5, 5, 5])}")



orig_list = [random.randint(-100, 100) for _ in range(10)]
# замеры 10
print(timeit.timeit("shellSort(orig_list)",
    setup="from __main__ import shellSort, orig_list", number=100))

orig_list = [random.randint(-100, 100) for _ in range(100)]
# замеры 100
print(timeit.timeit("shellSort(orig_list)",
    setup="from __main__ import shellSort, orig_list", number=100))

orig_list = [random.randint(-100, 100) for _ in range(1000)]
# замеры 1000
print(timeit.timeit("shellSort(orig_list)",
    setup="from __main__ import shellSort, orig_list", number=100))


orig_list = [random.randint(-100, 100) for _ in range(10)]
# замеры 10
print(timeit.timeit("lcl_median(orig_list)",
    setup="from __main__ import lcl_median, orig_list", number=100))

orig_list = [random.randint(-100, 100) for _ in range(100)]
# замеры 100
print(timeit.timeit("lcl_median(orig_list)",
    setup="from __main__ import lcl_median, orig_list", number=100))

orig_list = [random.randint(-100, 100) for _ in range(1000)]
# замеры 1000
print(timeit.timeit("lcl_median(orig_list)",
    setup="from __main__ import lcl_median, orig_list", number=100))


"""
Метод median выдает для списка с четным количеством элементов среднее значение между m/2 и (m/2)+1 эелементами
Для 2m + 1 списков - работает корректно

Исходный неотсортированный массив: [92, 55, -23, 19, -44, 83, -37, -19, 83, 15, -54]
Отсортированный массив: [-54, -44, -37, -23, -19, 15, 19, 55, 83, 83, 92]
Медиана из statistics: 15
Медиана моя для несортированного массива: 15
Исходный неотсортированный массив: [92, 55, -23, 19, -44, 83, -37, -19, 83, 15, -54]
Отсортированный массив методом Шелла: [-54, -44, -37, -23, -19, 15, 19, 55, 83, 83, 92]
Медиана моя для сортированного массива: 15
******************Нестандартные случаи:******************
Медиана моя для несортированного массива [3, 3, 3, 3, 3, 4, 5]: 3
Медиана моя для несортированного массива [3, 2, 5, 5, 5, 5, 5]: 5

Время, конечно, для поиска медианы в несортированном списке гораздно выше из-за сложности в худшем случае O(n2):
С сортировкой Шелла и выбираем средний элемент:
0.0005100999999999994
0.008618099999999997
0.1108691
Ищем медиану в несортированном:
0.00010969999999999036 - для малых может быть и быстрее
0.025368399999999985
8.016728
"""
