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

from memory_profiler import profile
from random import randint
import timeit


# @profile
def classic_bubble_sort(arr_len: int):
    N = arr_len
    a = []
    for i in range(N):
        a.append(randint(-100, 100))
    # print("Before sorting: {}".format(a))
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    # print("*After sorting: {}".format(a))


# @profile()
def bubble_sort_by_desc(arr_len: int):
    N = arr_len
    a = []
    # counter1 = 0
    # counter2 = 0
    for i in range(N):
        a.append(randint(-100, 100))
    # print("Before sorting: {}".format(a))
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                # counter2 += 1
        # if counter1 < counter2:
        #     counter1 = counter2
        # else:
        #     break

    # print("*After sorting: {}".format(a))


if __name__ == '__main__':
    arr_len = 10
    classic_bubble_sort(arr_len)
    print(timeit.timeit("classic_bubble_sort(arr_len)", setup="from __main__ import classic_bubble_sort, arr_len",
                        number=10000))
    print("- " * 50)
    bubble_sort_by_desc(arr_len)
    print(timeit.timeit("bubble_sort_by_desc(arr_len)", setup="from __main__ import bubble_sort_by_desc, arr_len",
                        number=10000))

"""
    В целом: оптимизация не дала большого эфекта, хотя на этапе, когда я просто начал делать обратную сортировку 
    наметился прогресс. 
    После того как я добавил проверку "была ли сортировка в проходе" - количество вхождений уменьшелось на некоторых прогонах
    , но эфект количества вхождения съедается дополнительной проверкой условного оператора if - else
    
    Ну и у меня есть сомнение, что я установил эту проверку в нужном месте.
    
    Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    20     13.1 MiB     13.1 MiB           1   @profile
    21                                         def classic_bubble_sort(arr_len: int):
    22     13.1 MiB      0.0 MiB           1       N = arr_len
    23     13.1 MiB      0.0 MiB           1       a = []
    24     13.1 MiB      0.0 MiB          11       for i in range(N):
    25     13.1 MiB      0.0 MiB          10           a.append(randint(-100, 100))
    26                                             # print("Before sorting: {}".format(a))
    27     13.1 MiB      0.0 MiB          10       for i in range(N - 1):
    28     13.1 MiB      0.0 MiB          54           for j in range(N - i - 1):
    29     13.1 MiB      0.0 MiB          45               if a[j] > a[j + 1]:
    30     13.1 MiB      0.0 MiB          24                   a[j], a[j + 1] = a[j + 1], a[j]

Время: 0.231115169

    Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    34     13.3 MiB     13.3 MiB           1   @profile()
    35                                         def bubble_sort_by_desc(arr_len: int):
    36     13.3 MiB      0.0 MiB           1       N = arr_len
    37     13.3 MiB      0.0 MiB           1       a = []
    38     13.3 MiB      0.0 MiB           1       counter1 = 0
    39     13.3 MiB      0.0 MiB           1       counter2 = 0
    40     13.3 MiB      0.0 MiB          11       for i in range(N):
    41     13.3 MiB      0.0 MiB          10           a.append(randint(-100, 100))
    42                                             # print("Before sorting: {}".format(a))
    43     13.3 MiB      0.0 MiB           4       for i in range(N - 1):
    44                                         
    45     13.3 MiB      0.0 MiB          34           for j in range(N - i - 1):
    46     13.3 MiB      0.0 MiB          30               if a[j] < a[j + 1]:
    47     13.3 MiB      0.0 MiB          11                   a[j], a[j + 1] = a[j + 1], a[j]
    48     13.3 MiB      0.0 MiB          11                   counter2 += 1
    49                                         
    50     13.3 MiB      0.0 MiB           4           if counter1 < counter2:
    51     13.3 MiB      0.0 MiB           3               counter1 = counter2
    52                                                 else:
    53     13.3 MiB      0.0 MiB           1               break

    Время: 0.23792687600000006

"""
