"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""
from memory_profiler import profile
from numpy import array
from pympler import asizeof


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r

    return g


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


@memorize
def recursive_reverse_memo(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse_memo(number // 10)}'


@profile
def recurs_stat(funс, number):
    funс(number)


if __name__ == "__main__":
    num = 10000000000000000000
    recurs_stat(recursive_reverse, num)
    recurs_stat(recursive_reverse_memo, num)

"""
Без мемоизации: 
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    33     30.9 MiB     30.9 MiB           1   @profile
    34                                         def recurs_stat(funс, number):
    35     30.9 MiB      0.0 MiB           1       funс(number)
    
С мемоизацией:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    33     30.9 MiB     30.9 MiB           1   @profile
    34                                         def recurs_stat(funс, number):
    35     31.0 MiB      0.1 MiB           1       funс(number)
"""
