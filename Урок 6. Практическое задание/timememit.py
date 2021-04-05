from functools import wraps
from time import perf_counter
from memory_profiler import memory_usage


def timememit(fun):
    @wraps(fun)
    def wrapper_timer(*args):
        mem0 = memory_usage()[0]
        t0 = perf_counter()
        ret = fun(*args)
        dmem = memory_usage()[0] - mem0
        dt = perf_counter() - t0
        print(f"{fun.__name__}: {dt:.4f} s, {dmem:4f} MiB")
        return ret
    return wrapper_timer
