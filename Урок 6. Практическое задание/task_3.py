"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""
########################################################################################################################

from memory_profiler import memory_usage, profile


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
even = []
uneven = []

m1 = memory_usage()


def rec_func(lst):
    if len(lst) == 0:
        return
    if lst[0] % 2 == 0:
        even.append(lst[0])
    else:
        uneven.append(lst[0])
    return rec_func(lst[1::])


rec_func(a)
m2 = memory_usage()
print(f'Память: {m2[0] - m1[0]}')
print(even, uneven)

"""
    При использовании @profile, выводятся данные на каждую итерацию, что довольно не удобно,
так что лучше использовать memory_usage. С увеличением массива, количество запрашиваемой рекурсией памяти
так же увеличивается.

"""
########################################################################################################################


@profile
def func_fib(n):
    if n < 2:
        return n
    return func_fib(n-2) + func_fib(n-1)


func_fib(5)

########################################################################################################################

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
even_sub = []
uneven_sub = []

m1_sub = memory_usage()


def rec_func(lst):
    if len(lst) == 0:
        return
    even_sub.append(lst[0]) if lst[0] % 2 == 0 else uneven_sub.append(lst[0])
    return rec_func(lst[1::])


rec_func(a)
m2_sub = memory_usage()
print(f'Память: {m2_sub[0] - m1_sub[0]}')
print(even_sub, uneven_sub)

"""
С помощью тернарного оператора удалось оптимизировать пример, и снизить память до нулей. 
"""