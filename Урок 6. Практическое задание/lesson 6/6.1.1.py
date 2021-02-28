
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

    def sum_rec(current_element_value, total_elements_count, result_sum: int = 0, current_element_index: int = 0):
        if current_element_index == total_elements_count:
            return result_sum
        elif current_element_index < total_elements_count:
            return sum_rec(-current_element_value/2, total_elements_count,
                                 result_sum + current_element_value, current_element_index + 1)

    while True:
        try:
            elements_count = int(input("Введите количество элементов > "))
            elements_sum = sum_rec(1, elements_count)
            print(f"Сумма: {elements_sum}")
        except ValueError:
            print("Число не является целым.")
            continue
        break


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