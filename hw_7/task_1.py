"""
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
from timeit import default_timer
import random
import memory_profiler


def decor(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        res_time = default_timer() - start_time
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff, res_time
    return wrapper


@decor
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


@decor
def bubble_sort_1(lst_obj):
    n = 1
    flag = True
    while n < len(lst_obj) and flag:
        flag = False
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                flag = True
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


print("При 10 элементах")
orig_list = [random.randint(-100, 99) for _ in range(10)]
res, mem_diff, res_time = bubble_sort(orig_list[:])
res1, mem_diff1, res_time1 = bubble_sort_1(orig_list[:])
print(orig_list)
print(res)
print(res1)
print(res_time)
print(res_time1)

print("При 100 элементах")
orig_list = [random.randint(-100, 99) for _ in range(100)]
res, mem_diff, res_time = bubble_sort(orig_list[:])
res1, mem_diff1, res_time1 = bubble_sort_1(orig_list[:])
print(res_time)
print(res_time1)

print("При 1000 элементах")
orig_list = [random.randint(-100, 99) for _ in range(1000)]
res, mem_diff, res_time = bubble_sort(orig_list[:])
res1, mem_diff1, res_time1 = bubble_sort_1(orig_list[:])
print(res_time)
print(res_time1)

print("При 10000 элементах")
orig_list = [random.randint(-100, 99) for _ in range(10000)]
res, mem_diff, res_time = bubble_sort(orig_list[:])
res1, mem_diff1, res_time1 = bubble_sort_1(orig_list[:])
print(res_time)
print(res_time1)

print("При 1000 элементах с сортировкой")
orig_list = [random.randint(-100, 99) for _ in range(1000)]
orig_list.sort(reverse=True)
res, mem_diff, res_time = bubble_sort(orig_list[:])
res1, mem_diff1, res_time1 = bubble_sort_1(orig_list[:])
print(res_time)
print(res_time1)

print("При 10000 элементах с сортировкой")
orig_list = [random.randint(-100, 99) for _ in range(10000)]
orig_list.sort(reverse=True)
res, mem_diff, res_time = bubble_sort(orig_list[:])
res1, mem_diff1, res_time1 = bubble_sort_1(orig_list[:])
print(res_time)
print(res_time1)

'''
Сделали сортировку пузырьком и пузырьком с улучшением, флагом, который срабатывает, если за один цикл по списку
перестановок не было, завершая сортировку. Улучшение действует эффективнор только на отсортированных
последовательностях. Если они перемешаны, то никакой выгоды на современных компьютерах не наблюдается.
Замеры:
При 10 элементах
0.09998
0.1003233
При 100 элементах
0.10145070000000006
0.10101780000000005
При 1000 элементах
0.20964559999999988
0.20808009999999988
При 10000 элементах
11.2774098
11.402891100000002
При 1000 элементах с сортировкой
0.15148859999999686
0.10034119999999902
При 10000 элементах с сортировкой
5.6823367000000005
0.10121180000000152
'''