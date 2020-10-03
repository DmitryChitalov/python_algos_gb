"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""
# Так профилировать достаточно сложно, так как при каждом вызове функции вызывается и декоратор
from memory_profiler import profile


@profile
def my_rec(num):
    if num == 1:
        return num
    else:
        res = num + my_rec(num-1)
    return res


print(my_rec(10))
