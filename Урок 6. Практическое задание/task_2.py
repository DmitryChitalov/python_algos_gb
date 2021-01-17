"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

from memory_profiler import profile
from collections import deque
from random import randint

# ------------------------ использование коллекции deque
num = []
for _ in range(1000000):
    num.append(randint(0, 10000))

lst = list(num)
dqe = deque(num)


# функция реализует вставку в список в начало и в конец

@profile
def lst_appender(l):
    for _ in range(10000):
        l.insert(0, randint(100, 1000))
    return l

# функция реализует вставку в деку в начало и в конец


@profile
def dqe_appender(d):
    for _ in range(10000):
        d.appendleft(randint(100, 1000))
    return d


if __name__ == "__main__":
    dqe_appender(dqe)
    lst_appender(lst)

# при проведении замеров обнаружилось, что при небольшом исходном списке на использование деки (вставка в начало)
# тратится примерно столько же памяти сколько и с применением обычного списка
# однако если исходный список очень большой, то в это случае использование деки очень сильно сокращает
# как время, так и занятую память

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
# 32     73.8 MiB     73.8 MiB           1   @profile
# 33                                         def dqe_appender(d):
# 34     74.1 MiB      0.0 MiB       10001       for _ in range(10000):
# 35     74.1 MiB      0.3 MiB       10000           d.appendleft(randint(100, 1000))
# 36     74.1 MiB      0.0 MiB           1       return d
#

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
# 24     74.1 MiB     74.1 MiB           1   @profile
# 25                                         def lst_appender(l):
# 26     82.0 MiB      0.0 MiB       10001       for _ in range(10000):
# 27     82.0 MiB      8.0 MiB       10000           l.insert(0, randint(100, 1000))
# 28     82.0 MiB      0.0 MiB           1       return l
