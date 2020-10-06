"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""
from memory_profiler import profile
from memory_profiler import memory_usage


@profile()
def reverse_f(num, res=0):
    if num < 10:
        return print(res * 10 + num)
    return reverse_f(num // 10, res * 10 + num % 10)


reverse_f(1253)


def reverse_f(num, res=0):
    if num < 10:
        return print(res * 10 + num)
    return reverse_f(num // 10, res * 10 + num % 10)


m1 = memory_usage()
reverse_f(1253)
m2 = memory_usage()
res = m2[0] - m1[0]

print(res)

# рекурсия вызывает профилер на каздом шаге рекурсии, не удобно.., но можно замерить память через memory usage
