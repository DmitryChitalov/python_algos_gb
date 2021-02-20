""""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
"""
0.1410718
0.14110040000000001
32.860875
32.407271400000006

Очевидно, что в том случае, когда за проход не проводится ни одной перестановки - массив
уже отсортирован. Такая оптимизация значительно улучшила производительность алгоритма.
Оптимизация обоснована, так как выполняются перестановки - т.е. вместе со "всплывающим" 
элементом другой, в свою очередь, "погружается", и эта операция на одном проходе выполняется 
для всех элементов после уже отсортированных. При этом, в случае частично отсортированных 
данных, что в реальности случается очень часто, оптимизация завершит алгоритм после первого 
же прохода без перестановок, в отличие от неоптимизированного, который безусловно перебирает 
весь массив данных
"""
from timeit import timeit
import random

def bubble_asc(in_arr):
    ind = 1
    stop_flag = False
    while ind < len(in_arr) and not stop_flag:
        stop_flag = True
        for i in range(len(in_arr) - ind):
            if in_arr[ i ] > in_arr[ i + 1 ]:
                tmp = in_arr[ i + 1 ]
                in_arr[ i + 1 ] = in_arr[ i ]
                in_arr[ i ] = tmp
                stop_flag = False
        ind += 1
    return in_arr

def bubble_desc(in_arr):
    ind = 1
    stop_flag = False
    while ind < len(in_arr) and not stop_flag:
        stop_flag = True
        for i in range(len(in_arr) - ind):
            if in_arr[ i ] < in_arr[ i + 1 ]:
                tmp = in_arr[ i + 1 ]
                in_arr[ i + 1 ] = in_arr[ i ]
                in_arr[ i ] = tmp
                stop_flag = False
        ind += 1
    return in_arr, ind

def bubble_asc_n(in_arr):
    ind = 1
    while ind < len(in_arr):
        for i in range(len(in_arr) - ind):
            if in_arr[ i ] > in_arr[ i + 1 ]:
                tmp = in_arr[ i + 1 ]
                in_arr[ i + 1 ] = in_arr[ i ]
                in_arr[ i ] = tmp
        ind += 1
    return in_arr

def bubble_desc_n(in_arr):
    ind = 1
    while ind < len(in_arr):
        for i in range(len(in_arr) - ind):
            if in_arr[ i ] < in_arr[ i + 1 ]:
                tmp = in_arr[ i + 1 ]
                in_arr[ i + 1 ] = in_arr[ i ]
                in_arr[ i ] = tmp
        ind += 1
    return in_arr

tot = 0
for i in range(10):
    num_arr = [random.randint(-100, 100) for _ in range(1000)]
    num_arr, ind = bubble_desc(num_arr)
    print(f'Cycles: {ind}')
    tot += ind
avg = tot // 10
print(f'Avg cycles: {avg}')
num_arr = [random.randint(-100, 100) for _ in range(1000)]
num_arr = bubble_desc_n(num_arr)

"""
num_arr = [random.randint(-100, 100) for _ in range(1000)]
print(
    timeit(
        "bubble_asc(num_arr)",
        setup='from __main__ import bubble_asc, num_arr',
        number=1000))
num_arr = [random.randint(-100, 100) for _ in range(1000)]
print(
    timeit(
        "bubble_desc(num_arr)",
        setup='from __main__ import bubble_desc, num_arr',
        number=1000))
num_arr = [random.randint(-100, 100) for _ in range(1000)]
print(
    timeit(
        "bubble_asc_n(num_arr)",
        setup='from __main__ import bubble_asc_n, num_arr',
        number=1000))
num_arr = [random.randint(-100, 100) for _ in range(1000)]
print(
    timeit(
        "bubble_desc_n(num_arr)",
        setup='from __main__ import bubble_desc_n, num_arr',
        number=1000))
"""
