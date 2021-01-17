"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from typing import Dict
from memory_profiler import profile
from random import randint
from collections import deque
import string

n = []
for _ in range(500000):
    n.append(randint(-5000, 5000))


@profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile
def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


if __name__ == "__main__":
    func_1(n)
    func_2(n)



# При сравнении двух данных решений по использованию памяти, большая часть памяти уходит на запуск профилирования,
# но по использованной памяти внутри функций выигрывает функция, в которой используется генераторное выражение
#  9,6 против 8,5 Mib

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
# 26     32.5 MiB     32.5 MiB           1   @profile
# 27                                         def func_1(nums):
# 28     32.5 MiB      0.0 MiB           1       new_arr = []
# 29     42.1 MiB      7.7 MiB      500001       for i in range(len(nums)):
# 30     42.1 MiB      0.0 MiB      500000           if nums[i] % 2 == 0:
# 31     42.1 MiB      1.9 MiB      250231               new_arr.append(i)
# 32     42.1 MiB      0.0 MiB           1       return new_arr
#
#
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
# 37     34.6 MiB     34.6 MiB           1   @profile
# 38                                         def func_2(nums):
# 39     43.1 MiB      8.5 MiB      500003       return [i for i in range(len(nums)) if nums[i] % 2 == 0]



companies = {}
for _ in range(10000000):
    companies[randint(400, 5000)] = randint(60000, 3000000000)


@profile
def top_companies2(dct: Dict[str, int]):
    a = sorted(dct.items(), key=lambda x: x[1], reverse=True)               # O(n log n)
    print(a[:3])


@profile
def top_companies3(dct: Dict[str, int]):
    lst_comp = list(dct.items())
    tops = sorted(list(lst_comp[:3]), key=lambda x: x[1], reverse=True)     # O(3), т.к всегда 3 значения
    for el in lst_comp:                                                     # O(n)
        if el[1] < tops[2][1]:                                              # O(1)
            continue                                                        # O(1)
        elif tops[2][1] < el[1] < tops[1][1]:                               # O(1)
            tops[2] = el                                                    # O(1)
        elif tops[1][1] < el[1] < tops[0][1]:                               # O(1)
            tops[1], tops[2] = tops[2], tops[1]                             # O(1)
            tops[1] = el                                                    # O(1)
        elif el[1] > tops[0][1]:                                            # O(1)
            tops[1], tops[2] = tops[2], tops[1]                             # O(1)
            tops[0], tops[1] = tops[1], tops[0]                             # O(1)
            tops[0] = el                                                    # O(1)

    print(tops)


if __name__ == "__main__":
    top_companies2(companies)
    top_companies3(companies)


# В данных задачах память затрачивается только на запуск профилирования, т.к данные внутри функции не записываются
# куда-либо, однако все же при сортировке словаря в первом случае затрачивается небольшое количество памяти
# около 0,2 MiB, при увеличении числа записей в словаре, затрачиваема памят не увеличивается

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
# 118     14.2 MiB     14.2 MiB           1   @profile
# 119                                         def top_companies2(dct: Dict[str, int]):
# 120     14.4 MiB      0.2 MiB        9203       a = sorted(dct.items(), key=lambda x: x[1], reverse=True)
# 121     14.4 MiB      0.0 MiB           1       print(a[:3])
#
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
# 124     14.4 MiB     14.4 MiB           1   @profile
# 125                                         def top_companies3(dct: Dict[str, int]):
# 126     14.4 MiB      0.0 MiB           1       lst_comp = list(dct.items())
# 127     14.4 MiB      0.0 MiB           7       tops = sorted(list(lst_comp[:3]), key=lambda x: x[1], reverse=True)
# 128     14.4 MiB      0.0 MiB        4602       for el in lst_comp:

# 129     14.4 MiB      0.0 MiB        4601           if el[1] < tops[2][1]:
# 130     14.4 MiB      0.0 MiB        4568               continue
# 131     14.4 MiB      0.0 MiB          33           elif tops[2][1] < el[1] < tops[1][1]:
# 132     14.4 MiB      0.0 MiB          10               tops[2] = el
# 133     14.4 MiB      0.0 MiB          23           elif tops[1][1] < el[1] < tops[0][1]:
# 134     14.4 MiB      0.0 MiB          13               tops[1], tops[2] = tops[2], tops[1]
# 135     14.4 MiB      0.0 MiB          13               tops[1] = el
# 136     14.4 MiB      0.0 MiB          10           elif el[1] > tops[0][1]:
# 137     14.4 MiB      0.0 MiB           7               tops[1], tops[2] = tops[2], tops[1]
# 138     14.4 MiB      0.0 MiB           7               tops[0], tops[1] = tops[1], tops[0]
# 139     14.4 MiB      0.0 MiB           7               tops[0] = el
# 140
# 141     14.4 MiB      0.0 MiB           1       print(tops)


num = []
for _ in range(10000000):
    num.append(randint(0, 10000))

lst = list(num)
dqe = deque(num)


# функция реализует вставку в список в начало и в конец

@profile
def lst_appender(l):
    l.insert(0, 'start')
    l.append('end')
    return l

# функция реализует вставку в деку в начало и в конец

@profile
def dqe_appender(d):
    d.appendleft('start')
    d.append('end')
    return d


if __name__ == "__main__":
    dqe_appender(dqe)
    lst_appender(lst)

# При сравнении использовании памяти при ставке в начало и конец списка с использованием простого списка и деки,
# оказалось, что использование деки не только ускоряет процесс вставки в начало,
# но и более оптимально по памяти
# increment вставки с использованием деки = 0
# increment вставки в обычный лист = 76,3 MiB


# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
# 160    554.9 MiB    554.9 MiB           1   @profile
# 161                                         def dqe_appender(d):
# 162    554.9 MiB      0.0 MiB           1       d.appendleft('start')
# 163    554.9 MiB      0.0 MiB           1       d.append('end')
# 164    554.9 MiB      0.0 MiB           1       return d
#

#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
# 152    554.9 MiB    554.9 MiB           1   @profile
# 153                                         def lst_appender(l):
# 154    631.2 MiB     76.3 MiB           1       l.insert(0, 'start')
# 155    631.2 MiB      0.0 MiB           1       l.append('end')
# 156    631.2 MiB      0.0 MiB           1       return l
