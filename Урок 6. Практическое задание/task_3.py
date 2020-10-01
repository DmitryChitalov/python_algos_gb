"""Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""


from memory_profiler import profile, memory_usage


# @profile()
def even_and_odd_digits(num: int, even=0, odd=0) -> list:
    even = 0
    odd = 0
    n = num
    while n > 0:
        if (n - (n // 10) * 10) % 2 != 0:
            odd += 1
        else:
            even += 1
        n = n // 10
        even_and_odd_digits(n, even, odd)
    return [even, odd]



n = 5
m1 = memory_usage()
even_and_odd_digits(n)
m2 = memory_usage()
mem_diff = m2[0] - m1[0]
print(f"Выполнение заняло {mem_diff} Mib")
# Выполнение заняло 0.0078125 Mib
"""Применение @profile() запускает замеры столько раз, какова глубина рекурсии. """
