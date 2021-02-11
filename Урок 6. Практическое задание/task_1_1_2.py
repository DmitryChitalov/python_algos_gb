"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import time
import functools


def timer(func):
    """to show make function time"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        delta_time = end_time - start_time
        print(f'func runtime is: {delta_time:.4f} sec')
        return value

    return wrapper_timer


@timer
def count_even_odd(num, even=0, odd=0):
    if (num % 10 % 2) == 0:
        even += 1
    else:
        odd += 1

    num = num // 10
    if num == 0:
        return even, odd
    else:
        return count_even_odd(num, even, odd)


print(count_even_odd(34560))
print(count_even_odd(123))
print(count_even_odd(0))
print()

def profiler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls = 0
        wrapper.calls += 1
        t = time.perf_counter()
        res = func(*args, **kwargs)
        t1 = (time.perf_counter() - t)

        return res

    wrapper.calls = 0
    return wrapper


@profiler
def count_even_odd(num, even=0, odd=0):
    if (num % 10 % 2) == 0:
        even += 1
    else:
        odd += 1

    num = num // 10
    if num == 0:
        return even, odd
    else:
        return count_even_odd(num, even, odd)


print(count_even_odd(34560))
print(count_even_odd(123))
print(count_even_odd(0))
