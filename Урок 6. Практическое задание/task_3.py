"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile


def fib(n):
    res = 1
    if n > 2:
        res = fib(n-1) + fib(n-2)
    return res

# Если делать профилировку напрямую рекурсивной функции, то мы полум профиль каждого вызова.
# Чтобы этого избежать, предлагаю использовать еще одну функцию, которая будет запускать рекурсию
# и ее профилировать
@profile
def fib_prof(n):
    return fib(n)


N = 30

if __name__ == "__main__":
    value = fib_prof(N)

print(f"{N} число Фибоначи = {value}")
