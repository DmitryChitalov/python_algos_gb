"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""
from memory_profiler import profile
import copy


@profile
def count_recur(i):
    y = [item for item in range(0, i, 2)]
    x = copy.deepcopy(y)
    z.append(x)
    del y
    del x
    print(z)
    if i <= 0:
        return
    count_recur(i - 1)


@profile
def start_recur(i):
    return count_recur(i)


global z
z = []
start_recur(100)

"""
Задание 3 *.
попытался сделать, но каждый вызов обсчитывается самостоятельно, как сделать общий не придумал
"""
