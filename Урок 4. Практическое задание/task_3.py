"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""

from cProfile import run
from timeit import timeit
from random import randint


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


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


nums = randint(1000, 10000)


"""
Функция revers_3 показывает наиболее эффективный способ реализции алгоритма со сложностью О(1)
Рекурсивный способ реализации revers_1, ожидаемо является самым медленным и не эфективным.
"""

print('--------- 1 Решение ------------')
run('revers_1(nums)')
print(
    timeit(
        'revers_1(nums)',
        setup='from __main__ import revers_1, nums',
        number=10000
    )
)
print('--------- 2 Решение ------------')
run('revers_2(nums)')
print(
    timeit(
        'revers_2(nums)',
        setup='from __main__ import revers_2, nums',
        number=10000
    )
)
print('--------- 3 Решение ------------')
run('revers_3(nums)')
print(
    timeit(
        'revers_3(nums)',
        setup='from __main__ import revers_3, nums',
        number=10000
    )
)

"""
--------- 1 Решение ------------
         8 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      5/1    0.000    0.000    0.000    0.000 task_3.py:21(revers_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


0.012481000000000006

--------- 2 Решение ------------
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:31(revers_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


0.009057399999999993
--------- 3 Решение ------------
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:39(revers_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


0.0034666000000000002


"""
