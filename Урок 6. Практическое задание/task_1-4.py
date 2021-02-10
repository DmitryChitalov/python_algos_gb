from memory_profiler import memory_usage
from timeit import default_timer
from random import randint


def measure(func):
    def wrapper(*args, **kwargs):
        t1 = default_timer()
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        t2 = default_timer()
        mem_diff = m2[0] - m1[0]
        tim_diff = t2 - t1
        return res, mem_diff, tim_diff
    return wrapper


@measure
def get_rand_str_0(nums):
    new_arr = ''
    for rec in range(10000):
        new_arr = f'{new_arr}-{randint(100000, 999999)}'
    return new_arr

@measure
def get_rand_str_1(nums):
    new_arr = ''
    for rec in [randint(100000, 999999) for i in range(10000)]:
        new_arr = f'{new_arr}-{rec}'
    return new_arr

@measure
def get_rand_str_2(nums):
    new_arr = ''
    for rec in (randint(100000, 999999) for i in range(10000)):
        new_arr = f'{new_arr}-{rec}'
    return new_arr

g_res, g_mem, g_tim = get_rand_str_0(list(range(100000)))
print(f"Выполнение заняло {g_mem} Mib, {g_tim} сек.")
g_res, g_mem, g_tim = get_rand_str_1(list(range(100000)))
print(f"Выполнение заняло {g_mem} Mib, {g_tim} сек.")
g_res, g_mem, g_tim = get_rand_str_2(list(range(100000)))
print(f"Выполнение заняло {g_mem} Mib, {g_tim} сек.")
# Задача: вернуть список случайных чисел.
# get_rand_str_0 - с использованием цикла for и генераторов.
# get_rand_str_1 - с использованием list comprehension.
# get_rand_str_2 - с использованием генераторов в полной мере.
# Вывод данной задачи:
# Выполнение заняло 0.21875 Mib, 0.23242929999999998 сек.
# Выполнение заняло 0.765625 Mib, 0.22243440000000003 сек.
# Выполнение заняло 0.140625 Mib, 0.22804590000000002 сек.
# Числа возвращены через строку(ее можно потом распарсить),
# а не через список.
# Вывод: генераторы оптимизированы по памяти лучше всего
# и их максимально рекомендуется использовать.
# Разрядность ОС: 64, python версии 3.9.0.
