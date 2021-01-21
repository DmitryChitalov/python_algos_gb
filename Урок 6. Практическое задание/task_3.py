"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
import time

from memory_profiler import memory_usage


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        m_start = memory_usage()
        res = func(*args, **kwargs)
        m_end = memory_usage()
        end = time.time()
        print(f'method => {func.__name__}\n\ttime => {end - start} sec, memory => {m_end[0] - m_start[0]}')
        return res

    return wrapper


def count_odd_even(num, counter):
    if num != 0:
        number = num % 10
        if number % 2 == 0:
            counter[0] += 1
        else:
            counter[1] += 1
        return count_odd_even(num // 10, counter)
    else:
        return counter


@benchmark
def wrapper_for_recursive(num, counter):
    return count_odd_even(num, counter)


try:
    num_from_input = int(input('Введите число:'))
    result = wrapper_for_recursive(num_from_input, [0, 0])
    print(f'Кол-во четных {result[0]}, нечетных {result[1]}')
except ValueError:
    print('Вы ввели не число!')

"""
Для профилирования рекурсивных функций достаточно использовать метод-обертку над рекурсией
"""
