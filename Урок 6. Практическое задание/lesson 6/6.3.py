
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
    def factorial(n = 987):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    factorial()



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


# если мы будем исследовать рекурсию - то при каждой итерации будет вызываться декоратор и выводиться отчёт,
# что будет неудобно для анализа

# Для того, чтобы не получать полотно нечитабельных данных при исследовании , мы можем просто обернуть её в
# функцию и исследовать уже эту функцию

# Поскольку сама функция вызывается лишь раз, то и отчёт будет один
# а из-за того, что в ней ничего нет, кроме рекурсии, мы получим только один отчёт

