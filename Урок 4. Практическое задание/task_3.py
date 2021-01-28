"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

from cProfile import run
from timeit import timeit
from random import randint

my_nums = randint(10000, 100000)


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


print('--------First solution--------')
run('revers(my_nums)')
print(
    timeit(
        'revers(my_nums)',
        setup='from __main__ import revers, my_nums',
        number=10000))

print('--------Second solution--------')
run('revers_2(my_nums)')
print(
    timeit(
        'revers_2(my_nums)',
        setup='from __main__ import revers_2, my_nums',
        number=10000))

print('--------Third solution--------')
run('revers_3(my_nums)')
print(
    timeit(
        'revers_3(my_nums)',
        setup='from __main__ import revers_3, my_nums',
        number=10000))

"""
    Наиболее эффективный способ реализации алгоритма - функция {revers_3}, сложность О(1).
    Наиболее затратный алгоритм - {revers} - рекурсия, которая вызывалась 6 раз.
    
****************************************************************************************************    
*D:/Stydy/GeekBrain/Python_2/Lesson_4/les_4-task-3.py
*--------First solution--------
*  9 function calls (4 primitive calls) in 0.000 seconds
*  Ordered by: standard name
*   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
*        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
*      6/1    0.000    0.000    0.000    0.000 les_4-task-3.py:20(revers)
*        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
*        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
*
*   timeit - 0.012668800000000001
*
*--------Second solution--------
*   4 function calls in 0.000 seconds
*   Ordered by: standard name
*   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
*        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
*        1    0.000    0.000    0.000    0.000 les_4-task-3.py:30(revers_2)
*        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
*        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
*
*   timeit - 0.008414899999999996
*
*--------Third solution--------
*   4 function calls in 0.000 seconds
*   Ordered by: standard name
*   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
*        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
*        1    0.000    0.000    0.000    0.000 les_4-task-3.py:38(revers_3)
*        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
*        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
*
*   timeit - 0.0030694
****************************************************************************************************
"""