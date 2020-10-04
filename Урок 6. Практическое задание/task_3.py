"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""

from memory_profiler import profile


@profile
def f(m):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    return factorial(m)


print(f(54))
# на рекурсию уходит больше памяти, т.к. при ее работе хранится стэк вызываемых функций
