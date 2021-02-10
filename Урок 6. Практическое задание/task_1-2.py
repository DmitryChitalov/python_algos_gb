from memory_profiler import memory_usage
from timeit import default_timer
from numpy import array


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
def get_sim_erat_1(i_ind):
    a = []
    n = i_ind
    n = n * 30
    for i in range(n + 1):
            a.append(i)
    a[1] = 0

    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1

    res = []
    for rec in a:
        if rec != 0:
            res.append(rec)
    return res[i_ind - 1]


@measure
def get_sim_erat_2(i_ind):
    n = i_ind
    n = n * 30
    a = array(range(n + 1), int)
    for i in range(n + 1):
        a[i] = i
    a[1] = 0

    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1

    res = []
    for rec in a:
        if rec != 0:
            res.append(rec)
    return res[i_ind - 1]

g_res, g_mem, g_tim = get_sim_erat_1(1000000)
print(f"-{g_res}-Выполнение заняло {g_mem} Mib, {g_tim} сек.")
g_res, g_mem, g_tim = get_sim_erat_2(1000000)
print(f"-{g_res}-Выполнение заняло {g_mem} Mib, {g_tim} сек.")
# Задача: посчитать i-е по счёту простое число
# применив алгоритм "Решето эратосфена".
# get_sim_erat_1 - неоптимизированный вариант.
# get_sim_erat_2 - оптимизированный вариант.
# Вывод данной задачи:
#-15485863-Выполнение заняло 0.890625 Mib, 17.0820531 сек.
#-15485863-Выполнение заняло 0.36328125 Mib, 27.966300500000003 сек.
# Оптимизация произведена по памяти(get_sim_erat_2) за счет того, что
# применен массив из библиотеки numpy,
# а не через встроенный стандартный список list.
# Разрядность ОС: 64, python версии 3.9.0.
