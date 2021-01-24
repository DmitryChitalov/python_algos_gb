""""
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def new_bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        change_place = True
        for i in range(len(lst_obj) - n):
            if not change_place:
                break
            change_place = False

            for j in range(len(lst_obj) - n):
                if lst_obj[j] < lst_obj[j + 1]:
                    lst_obj[j], lst_obj[j + 1] = lst_obj[j + 1], lst_obj[j]
        n += 1
    return lst_obj



orig_list = [random.randint(-100, 100) for _ in range(1000)]
# print(orig_list)
# массив 1000
print(timeit.timeit("bubble_sort(orig_list)",
                    setup="from __main__ import bubble_sort, orig_list", number=1))
print(timeit.timeit("new_bubble_sort(orig_list)",
                    setup="from __main__ import new_bubble_sort, orig_list", number=1))


orig_list_1 = [random.randint(-100, 100) for _ in range(10000)]
# print(orig_list)
# массив 10000
print(timeit.timeit("bubble_sort(orig_list_1)",
                    setup="from __main__ import bubble_sort, orig_list_1", number=1))
print(timeit.timeit("new_bubble_sort(orig_list_1)",
                    setup="from __main__ import new_bubble_sort, orig_list_1", number=1))


orig_list_2 = [random.randint(-100, 100) for _ in range(20000)]
# print(orig_list)
# массив 20000
print(timeit.timeit("bubble_sort(orig_list_2)",
                    setup="from __main__ import bubble_sort, orig_list_2", number=1))
print(timeit.timeit("new_bubble_sort(orig_list_2)",
                    setup="from __main__ import new_bubble_sort, orig_list_2", number=1))

'''
После доработки код работает примерно в два раза быстрее.
0.0574673 - без доработки массив 1000
0.030609599999999987 - с доработкой массив 1000
5.9143083 - без доработки массив 10000
2.9592837999999997 - с доработкой массив 10000
23.640575600000002 - без доработки массив 20000
12.054051000000001 - с доработкой массив 20000
'''