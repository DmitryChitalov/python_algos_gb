"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""
"""
Подводные камни есть, у меня профилировка через декоратор, вообще ничего не выдаёт.
Ну а обойти как я и уже сказал в первом варинанте можно чрез отсечки.
"""


import memory_profiler
from memory_profiler import profile


@profile
def rec_fibo(n=7):
    if n <= 1:
        return n
    return rec_fibo(n - 1) + rec_fibo(n - 2)


m1 = memory_profiler.memory_usage()


def rec_fibo_v2(n=7):
    if n <= 1:
        return n
    return rec_fibo(n - 1) + rec_fibo(n - 2)


m2 = memory_profiler.memory_usage()
print(f'Memory - {m2[0] - m1[0]}')
