from memory_profiler import memory_usage
import timeit
from functools import wraps


def measurer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = timeit.default_timer()
        m1 = memory_usage()
        func(*args, **kwargs)
        t2 = timeit.default_timer()
        m2 = memory_usage()
        return print(f'Выполнение заняло {(t2 - t1):.05} сек и {(m2[0] - m1[0]):.04} Miб')
    return wrapper