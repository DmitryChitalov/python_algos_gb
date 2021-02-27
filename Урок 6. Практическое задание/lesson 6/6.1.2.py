
from memory_profiler import profile, memory_usage
import time
import csv
import cProfile


def time_memory_decorator(tmd):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        m1 = memory_usage()
        ans = tmd(*args, **kwargs)
        print(f'Время выполнения: {time.time() - time_start}')
        m2 = memory_usage()
        print(f'Расход памяти: {m2[0] - m1[0]}')
        return ans

    return wrapper


def profile2(func):
    def wrapper(*args, **kwargs):
        profile_filename = func.__name__ + '.prof'
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        return result
    return wrapper


@time_memory_decorator
def prof():
    # n = int(input("Введите n - натуральное число "))
    n = 987

    def first(n):
        if n == 1:
            return n
        elif n > 0:
            return n + first(n - 1)

    def second(n):
        return n * (n + 1) // 2

    if first(n) == second(n):
        print(f'Для n={n} - True')
    else:
        print(f'Для n={n} - False')


def start():
    def start_pr1():
        prof()
        print()

    @profile
    def start_pr2():
        prof()
        print()

    @profile2
    def start_pr3():
        prof()
        print()

    start_pr1()
    start_pr2()
    start_pr3()


start()



# "C:\Program Files\Python39\python.exe" "C:/Users/YAROSLAR/OneDrive - AMDOCS/Backup Folders/Desktop/Рабочие файлы/lesson 6/6.1.2.py"
# Для n=987 - True
# Время выполнения: 0.10227394104003906
# Расход памяти: 1.39453125
#
# Для n=987 - True
# Время выполнения: 0.10562801361083984
# Расход памяти: 0.8046875
#
# Filename: C:\Users\YAROSLAR\OneDrive - AMDOCS\Backup Folders\Desktop\Рабочие файлы\lesson 6\6.1.2.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     56     17.6 MiB     17.6 MiB       @profile
#     57                                 def start_pr2():
#     58     18.5 MiB      0.8 MiB           prof()
#     59     18.5 MiB      0.0 MiB           print()
#
#
# Для n=987 - True
# Время выполнения: 0.10210227966308594
# Расход памяти: 0.1328125
#
#
# Process finished with exit code 0


# Встроенный декоратор cProfile позволил в 10 раз уменьшил расход памяти
# memory_profiler - уменьшил примерно на 45% расход памяти

# Время исполнения в пределах погрешности

# Вариант оптимизации через cProfiler в данном случае предпочтителен


