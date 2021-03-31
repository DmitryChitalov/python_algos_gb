"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from cProfile import Profile
from pstats import Stats
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


n = 846207850378
N = 100000

profiler = Profile()
profiler.enable()
for i in range(N):
    revers(n)
    revers_2(n)
    revers_3(n)
profiler.disable()
Stats(profiler).strip_dirs().print_stats()
# ---
#    1500001 function calls (300001 primitive calls) in 0.744 seconds
#
#    Random listing order was used
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 1300000/
#    100000    0.488    0.000    0.488    0.000 task_3.py:17(revers)
#    100000    0.209    0.000    0.209    0.000 task_3.py:27(revers_2)
#    100000    0.047    0.000    0.047    0.000 task_3.py:35(revers_3)
# ---


print("revers\t\t", timeit("revers(n)", globals=globals(), number=N))
print("revers_2\t", timeit("revers_2(n)", globals=globals(), number=N))
print("revers_3\t", timeit("revers_3(n)", globals=globals(), number=N))
# ---
# revers	0.29492326197214425
# revers_2	0.20011793699814007
# revers_3	0.03318392898654565
# ---

# Встроенная функция предсказуемо лидирует в двух испытаниях.
# Остается неясным, почему cProfile и timeit дают разное
# отношение времен для цикла и рекурсии, cProfile дает 2,
# а timeit дает 1.5 Мне кажется, доверять нужно timeit,
# как самому "тупому" и поэтому надежному методу.
#
# cProfile строит свою статистику на основе измерений вызовов
# всех функций. Очевидно, при таком подходе чаще всего
# вызывается revers_2(0). При усреднении это приводит
# к занижению результатов по времени.
