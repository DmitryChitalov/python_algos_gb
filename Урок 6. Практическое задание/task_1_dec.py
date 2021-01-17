from memory_profiler import memory_usage
from time import perf_counter


def mem_time_check(func):
    def wrapper():
        start = perf_counter()
        mem = memory_usage()
        func()
        print(f'Время выполнения функции заняло {perf_counter() - start} сек.')
        print(f'Для этого потребовалось {memory_usage()[0] - mem[0]} MiB')
    return wrapper()


@mem_time_check
def func_1():  # O(n)
    nums = list(range(500000))
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    del nums
    return new_arr


"""
Время выполнения функции заняло 0.17321709999999998 сек.
Для этого потребовалось 2.1796875 MiB
"""
