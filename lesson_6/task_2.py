"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика)
"""
import random
from pympler import asizeof
from functools import reduce
import memory_profiler

lst = [random.randint(1, 100) for i in range(100000)]
#print(lst)
print('размер списка')
print(asizeof.asizeof(lst))

#lstnew = list(map(int, lst))
print('размер кортежа')
lstnew = {random.randint(1, 100) for i in range(100000)}
#print(lstnew)
print(asizeof.asizeof(lstnew))



def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


@decor
def sumall(lst):
    return reduce(lambda x, y: x * y, lst)


@decor
def sumall_1(l):
    s = 0
    for i in l:
        s += s * i
    return s


print('sumall')
res, mem_diff = sumall(lst)
print(f"Выполнение заняло {mem_diff} Mib")

print('sumall_1')
res1, mem_diff1 = sumall_1(lstnew)
print(f"Выполнение заняло {mem_diff1} Mib")



'''
Кортеж использует памяти в 9 раз меньше списков
размер списка
804184
размер кортежа
11608
sumall

Другие идеи не получилось доказать (

'''
