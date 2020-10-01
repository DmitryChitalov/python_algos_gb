"""
Задание 3.
Сделать профилировку для скриптов с рекурсией и сделать вывод, можно ли
так профилировать или есть "подводные камни".
"""
from timeit import timeit
import cProfile


# class CheckRec:
#     def __init__(self, max_calls=1):
#         self._max_calls = max_calls
#         self._now_calls = 0

#     def new_profile(self, func):
#         if self._now_calls < self._max_calls:
#             self._now_calls += 1
#             return profile(func=func)


# @prof.new_profile
def sum_list(lst):
        if lst:
            new_list = lst[1:]
            return lst[0] + sum_list(new_list)
        else:
            return 0


cProfile.run('sum_list(range(20))')
result_1 = timeit("sum_list(range(20))", "from __main__ import sum_list", number=100000)
print(f'Результат выполнения sum_list(): {result_1} сек.')

"""
При использовании декоратора @memory_profiler.profile отчет по анализу фукнции вызывается каждый раз
при вызове функции внутри рекурсии. Я хотел исправить это, выполнив перегрузку
операторов __iter__ и __next__, но потом понял, что это не принесет ничего полезного (+ оказывается,
profile является не классом, а функцией).
Потом пробовал написать свой декоратор через class CheckRec, чтобы контролировать количество вызовов
memory_profiler.profile, но это также не принесло результатов.
Поэтому для профилирования рекурсивных функций лучше использовать timeit и cProfile.

         24 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     21/1    0.000    0.000    0.000    0.000 task_3.py:24(sum_list)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Результат выполнения sum_list(): 0.8386973200000001 сек.
"""
