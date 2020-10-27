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


print(f(100))
# на рекурсию уходит больше памяти, т.к. при ее работе хранится стэк вызываемых функций
"""При попытке применить profile() напрямую к функции, которая рекурсивно вызывается возникает ошибка,
поэтому для замера функцию приходиться 'оборачивать' в другую функцию, как в примере выше.
@profile
def x_factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(x_factorial(54))
"""