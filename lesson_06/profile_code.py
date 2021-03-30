from memory_profiler import memory_usage
from timeit import default_timer


def profile_code(num=1000000):
    def profile_dec(func):
        def wrapper(*args, **kwargs):
            result_time = 0
            result_mem = 0
            result = None
            for _ in range(num):
                start_time = default_timer()
                start_mem = memory_usage()[0]
                result = func(*args, **kwargs)
                delta_mem = memory_usage()[0] - start_mem
                delta_time = default_timer() - start_time
                result_mem += delta_mem
                result_time += delta_time
            print(f'Время: {result_time}, Память: {result_mem}')
            return result
        return wrapper
    return profile_dec
