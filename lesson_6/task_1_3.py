from memory_profiler import profile
import memory_profiler


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


@decor
def gen_num(n):
    nn = n
    for i in range(1, n):
        nn += 1
        yield nn

res, mem_diff = [x for x in gen_num(200000)]
for i in res:
    print(i)

print(f"Выполнение заняло {mem_diff} Mib")



@profile
def gen_lst_in(n):
    lst = [x for x in range(n)]
    return lst


lstlst = gen_lst_in(200000)
#print(lstlst)

"""
профилирование через profile почему то не работает для функций c генераторами,  где есть yield.
Пришлось использовать memory_usage через декоратор.
Выполнение заняло 0.00390625 Mib


List comprehension замерял через  profile
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     19.4 MiB     19.4 MiB           1   @profile
    29                                         def gen_lst_in(n):
    30     27.9 MiB  -9043.9 MiB      200003       lst = [x for x in range(n)]
    31     27.9 MiB      0.0 MiB           1       return lst


По результатам, генераторы списков значительно быстрее циклов или List comprehension



"""