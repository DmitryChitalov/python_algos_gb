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
import statistics
import timeit


def arr_init(arr_length: int):
    arr = []
    for i in range(arr_length):
        arr.append(randint(1, 100))
    return arr


def classic_bubble_sort(arr: list):
    a = arr
    # print("Before sorting: {}".format(arr))
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    # print("*After sorting: {}".format(arr))
    if len(a) % 2 == 0:
        return sum(a) / len(a)
    else:
        return a[int(len(a)/2)]


def shellSort(array_list: list) -> list:
    sublistcount = len(array_list) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(array_list, startposition, sublistcount)

        sublistcount = sublistcount // 2
    if len(array_list) % 2 == 0:
        return sum(array_list) / len(array_list)
    else:
        return array_list[int(len(array_list)/2)]


def gapInsertionSort(arr_list, start, gap):
    for i in range(start + gap, len(arr_list), gap):
        current_value = arr_list[i]
        position = i

        while position >= gap and arr_list[position - gap] > current_value:
            arr_list[position] = arr_list[position - gap]
            position = position - gap

        arr_list[position] = current_value


def find_mediana_without_sorting(arr: list) -> int:
    avg_sum = sum(arr) // len(arr)
    # print("Среднее значение = {}".format(avg_sum))
    for i in reversed(range(len(arr))):
        if arr[i] > avg_sum:
            num = arr.pop(i)
            # print("Выкидываем {}".format(num))
    return max(arr)


def get_median(arr: list):
    return statistics.median(arr)


if __name__ == '__main__':
    arr_len = 11
    static_arr = [10, 22, 8, 23, 90, 21, 4, 55, 98, 45, 11]
    my_arr = arr_init(arr_len)

    # print("Медиана списка (bubble_sort): {}".format(classic_bubble_sort(static_arr[:])))
    #
    # print("Медиана списка (shellSort): {}".format(shellSort(static_arr[:])))
    #
    # print("Медиана списка (without_sorting): {}".format(find_mediana_without_sorting(static_arr[:])))
    #
    # print("Медиана списка (get_median): {}".format(get_median(static_arr[:])))
    times = 10000
    print(timeit.timeit("classic_bubble_sort(static_arr[:])",
                        setup="from __main__ import classic_bubble_sort, static_arr", number=times))
    print(timeit.timeit("shellSort(static_arr[:])",
                        setup="from __main__ import shellSort, static_arr", number=times))
    print(timeit.timeit("find_mediana_without_sorting(static_arr[:])",
                        setup="from __main__ import find_mediana_without_sorting, static_arr", number=times))
    print(timeit.timeit("get_median(static_arr[:])",
                        setup="from __main__ import get_median, static_arr", number=times))
    """
    По результатам замера видно что пузырек здорово проседает.
    Шелл - тоже не айс, а на больших величинах дак и всовсем просел 
    Довольно не плохо себя показал способ без сортировки - в принципе ожидаемо
    
        number=100
            0.002128724999999998
            0.0015021409999999985
            0.00023840800000000245
            0.00015083800000000036
        
        number=10000
            0.139103704
            0.12195975999999997
            0.024286175999999993
            0.00878616900000001
    """