"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""

from memory_profiler import profile

length = 900


@profile
def recursion(length):
    def sum_seriesnumbers(n, elem=1):
        if n <= 0:
            return 0
        return elem + sum_series_numbers(n - 1, -elem / 2)

    print(f'{length} равна {sum_seriesnumbers(length)}')


@profile
def for_in(length):
    elem = 1
    amount = 0
    for i in range(length):
        amount += elem
        elem = -elem / 2
    print(f'{length} равна {sum_seriesnumbers(length)}')
