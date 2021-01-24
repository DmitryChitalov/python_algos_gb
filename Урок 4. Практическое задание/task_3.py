"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""


from timeit import timeit
import cProfile
from random import randint


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


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

# 0.0203743 - алгоритм через рекурсию - дольше всех
print(
    timeit(
        "revers(num_100)",
        setup='from __main__ import revers, num_100',
        number=10000))

print(
    timeit(
        "revers(num_1000)",
        setup='from __main__ import revers, num_1000',
        number=10000))

print(
    timeit(
        "revers(num_10000)",
        setup='from __main__ import revers, num_10000',
        number=10000))

print('*' * 20)

# 0.013176 - арифметические операции -
print(
    timeit(
        "revers_2(num_100)",
        setup='from __main__ import revers_2, num_100',
        number=10000))

print(
    timeit(
        "revers_2(num_1000)",
        setup='from __main__ import revers_2, num_1000',
        number=10000))

print(
    timeit(
        "revers_2(num_10000)",
        setup='from __main__ import revers_2, num_10000',
        number=10000))

print('*' * 20)

# 0.0035549000000000067 - быстрее всего, т.к. используется больше всего встроенные функции, чем больше n, тем нагляднее
print(
    timeit(
        "revers_3(num_100)",
        setup='from __main__ import revers_3, num_100',
        number=10000))

print(
    timeit(
        "revers_3(num_1000)",
        setup='from __main__ import revers_3, num_1000',
        number=10000))

print(
    timeit(
        "revers_3(num_10000)",
        setup='from __main__ import revers_3, num_10000',
        number=10000))


def main():
    for i in range(10000):
        revers(num_100)
        revers(num_1000)
        revers(num_10000)

        revers_2(num_100)
        revers_2(num_1000)
        revers_2(num_10000)

        revers_3(num_100)
        revers_3(num_1000)
        revers_3(num_10000)


cProfile.run('main()')

""" видно, что функция revers - рекурсивная
         39 function calls (13 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:109(main)
     29/3    0.000    0.000    0.000    0.000 task_3.py:19(revers)
        3    0.000    0.000    0.000    0.000 task_3.py:29(revers_2)
        3    0.000    0.000    0.000    0.000 task_3.py:37(revers_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Для наглядности увеличил количество запусков функций, иначе всё по нулям

         350004 function calls (90004 primitive calls) in 0.248 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.248    0.248 <string>:1(<module>)
        1    0.022    0.022    0.248    0.248 task_3.py:109(main)
290000/30000    0.143    0.000    0.143    0.000 task_3.py:19(revers)
    30000    0.069    0.000    0.069    0.000 task_3.py:29(revers_2)
    30000    0.014    0.000    0.014    0.000 task_3.py:37(revers_3)
        1    0.000    0.000    0.248    0.248 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""