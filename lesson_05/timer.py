from timeit import default_timer


def timer(num=1000000):
    """Декоратор с параметром (число повторений) для подсчёта суммарного времени выполнения функции"""
    def time_dec(func):
        def wrapper(*args):
            result_time = 0
            result = None
            for _ in range(num):
                start = default_timer()
                result = func(*args)
                delta_time = default_timer() - start
                result_time += delta_time
            print(result_time)
            return result
        return wrapper
    return time_dec
