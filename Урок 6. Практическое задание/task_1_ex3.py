from memory_profiler import profile
import timeit


@profile()
def func_1():  # O(n)
    nums = list(range(500000))
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    del nums
    return new_arr


func_1()


"""
при запуске програмы выделено 19.6 MiB
для создания списка выделено еще 19.3 MiB 
еще 10.3 MiB выделено для диапозона строка 9
после отработки цикла for in удаляем nums и освобождаем 18.8 MiB 

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     5     19.6 MiB     19.6 MiB           1   @profile()
     6                                         def func_1():  # O(n)
     7     38.9 MiB     19.3 MiB           1       nums = list(range(500000))
     8     38.9 MiB      0.0 MiB           1       new_arr = []
     9     48.6 MiB -65222.4 MiB      500001       for i in range(len(nums)):
    10     48.6 MiB -65214.7 MiB      500000           if nums[i] % 2 == 0:
    11     48.6 MiB -32608.5 MiB      250000               new_arr.append(i)
    12     29.8 MiB    -18.8 MiB           1       del nums
    13     29.8 MiB      0.0 MiB           1       return new_arr

"""