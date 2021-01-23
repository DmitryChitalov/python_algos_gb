"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile


@profile
def test_recursive_func(func):
    def wrapper(number):
        result = func(number)
        return result
    return wrapper


@test_recursive_func
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print(recursive_reverse(1234567892435465))
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     15.9 MiB     15.9 MiB           1   @profile
    12                                         def recursive_reverse(number):
    13     15.9 MiB      0.0 MiB           1       if number == 0:
    14     15.9 MiB      0.0 MiB           1           return str(number % 10)
    15                                             return f'{str(number % 10)}{recursive_reverse(number // 10)}'

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     15.9 MiB     15.9 MiB           2   @profile
    12                                         def recursive_reverse(number):
    13     15.9 MiB      0.0 MiB           2       if number == 0:
    14     15.9 MiB      0.0 MiB           1           return str(number % 10)
    15     15.9 MiB      0.0 MiB           1       return f'{str(number % 10)}{recursive_reverse(number // 10)}'

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     15.9 MiB     15.9 MiB           3   @profile
    12                                         def recursive_reverse(number):
    13     15.9 MiB      0.0 MiB           3       if number == 0:
    14     15.9 MiB      0.0 MiB           1           return str(number % 10)
    15     15.9 MiB      0.0 MiB           2       return f'{str(number % 10)}{recursive_reverse(number // 10)}'

Использование профилировщика для рекурсивных функций, осуществляет вывод множественный вывод аналитики по памяти равной
количеству итераций в цикле.
Для оптимизации кода, необходимо обернуть функциию в другой декоратор и выолпнить профилировку созданного декоратора.
В резульатте мы поулчаем один вывод профилировщика с информацией об использованной памяти 

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     15.9 MiB     15.9 MiB           1   @profile
    12                                         def test_recursive_func(func):
    13     15.9 MiB      0.0 MiB           1       def wrapper(number):
    14                                                 result = func(number)
    15                                                 return result
    16     15.9 MiB      0.0 MiB           1       return wrapper
"""