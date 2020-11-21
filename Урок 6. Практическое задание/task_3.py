"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile


@profile
def recur_wrapper():
    n = int(input('Введите число: '))

    def recur_sum(n, x=1, result=1):
        if n == 1:
            print(result)
        else:
            n -= 1
            x = x / 2 * (-1)
            result = result + x
            return recur_sum(n, x, result)
    return recur_sum(n)


recur_wrapper()